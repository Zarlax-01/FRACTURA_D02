# FRACTURA.Δ02 - Improved Script Suite
# Enhanced version with better error handling, logging, and modularity

import json
import os
import sys
import subprocess
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
from random import shuffle
from datetime import datetime

# =============================================================================
# CORE UTILITIES MODULE (lux_utils.py)
# =============================================================================

class LuxUtils:
    """Core utilities for FRACTURA.Δ02 project file management and operations."""
    
    def __init__(self):
        self.setup_logging()
        self.base_path = self._get_base_path()
        self.ensure_directories()
    
    def setup_logging(self):
        """Configure logging for the entire project."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('fractura_debug.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def _get_base_path(self) -> Path:
        """Returns the absolute path to the project root directory."""
        # Navigate up from scripts directory to project root
        current_file = Path(__file__).resolve()
        if current_file.parent.name == 'scripts':
            return current_file.parent.parent
        else:
            # If running from project root
            return current_file.parent
    
    def get_json_path(self, filename: str = "FRACTURA.Δ02.json") -> Path:
        """Constructs path to JSON file in project root."""
        json_path = self.base_path / filename
        if not json_path.exists():
            # Try alternative naming convention
            alt_path = self.base_path / "FRACTURA_D02.json"
            if alt_path.exists():
                return alt_path
        return json_path
    
    def get_output_path(self, filename: str) -> Path:
        """Constructs path to file in outputs directory."""
        return self.base_path / "outputs" / filename
    
    def ensure_directories(self):
        """Create necessary directories if they don't exist."""
        outputs_dir = self.base_path / "outputs"
        outputs_dir.mkdir(exist_ok=True)
        self.logger.info(f"Ensured outputs directory exists: {outputs_dir}")
    
    def load_json_data(self) -> Optional[Dict[str, Any]]:
        """Load and validate the main JSON configuration file."""
        json_path = self.get_json_path()
        
        if not json_path.exists():
            self.logger.error(f"JSON file not found: {json_path}")
            return None
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.logger.info(f"Successfully loaded JSON from: {json_path}")
            return data
        
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON format: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Error loading JSON: {e}")
            return None

# =============================================================================
# SYMBOL EXTRACTION MODULE
# =============================================================================

class SymbolExtractor:
    """Extracts and processes symbolic content from FRACTURA configuration."""
    
    def __init__(self, utils: LuxUtils):
        self.utils = utils
        self.logger = utils.logger
    
    def extract_symbols(self) -> bool:
        """Extract symbols from JSON and write to output file."""
        self.logger.info("🔮 Starting symbol extraction process")
        
        # Load JSON data
        data = self.utils.load_json_data()
        if not data:
            return False
        
        # Extract symbols from multiple sources
        symbols = self._gather_all_symbols(data)
        
        if not symbols:
            self.logger.warning("No symbols found in JSON data")
            return False
        
        # Write to output file
        output_file = self.utils.get_output_path("symboles_extraits.txt")
        return self._write_symbols_file(symbols, output_file)
    
    def _gather_all_symbols(self, data: Dict[str, Any]) -> List[str]:
        """Gather symbols from all relevant sections of the JSON."""
        all_symbols = []
        
        # Get symbols from symbolic_analysis section
        symbolic_analysis = data.get("symbolic_analysis", {})
        
        # Core symbols
        symbols = symbolic_analysis.get("symbols", [])
        all_symbols.extend(symbols)
        
        # Aesthetic techniques (these are also symbolic)
        aesthetic_techniques = symbolic_analysis.get("aesthetic_techniques", [])
        all_symbols.extend(aesthetic_techniques)
        
        # Remove duplicates while preserving order
        unique_symbols = []
        seen = set()
        for symbol in all_symbols:
            if symbol not in seen:
                unique_symbols.append(symbol)
                seen.add(symbol)
        
        self.logger.info(f"Gathered {len(unique_symbols)} unique symbols")
        return unique_symbols
    
    def _write_symbols_file(self, symbols: List[str], output_file: Path) -> bool:
        """Write processed symbols to output file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("🔮 Symboles analysés dans FRACTURA.Δ02\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Extraction générée le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for i, symbol in enumerate(symbols, 1):
                    f.write(f"{i:2d}. {symbol}\n")
                
                f.write(f"\n--- Total: {len(symbols)} symboles ---\n")
            
            self.logger.info(f"✅ Symbols written successfully to: {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Error writing symbols file: {e}")
            return False

# =============================================================================
# MANTRA EXTRACTION MODULE
# =============================================================================

class MantraExtractor:
    """Extracts and processes mantra/narrative content from FRACTURA configuration."""
    
    def __init__(self, utils: LuxUtils):
        self.utils = utils
        self.logger = utils.logger
    
    def extract_mantras(self) -> bool:
        """Extract mantras from JSON and write to output file."""
        self.logger.info("🗝️ Starting mantra extraction process")
        
        # Load JSON data
        data = self.utils.load_json_data()
        if not data:
            return False
        
        # Extract mantras and related narrative elements
        mantras = self._gather_all_mantras(data)
        
        if not mantras:
            self.logger.warning("No mantras found in JSON data")
            return False
        
        # Write to output file
        output_file = self.utils.get_output_path("mantras_extraits.txt")
        return self._write_mantras_file(mantras, output_file)
    
    def _gather_all_mantras(self, data: Dict[str, Any]) -> List[str]:
        """Gather mantras and narrative elements from JSON."""
        all_mantras = []
        
        # Get from narrative_structures section
        narrative = data.get("narrative_structures", {})
        
        # Core mantras
        mantras = narrative.get("mantras", [])
        all_mantras.extend(mantras)
        
        # Add archetype description as a meta-mantra
        archetype = narrative.get("archetype", "")
        if archetype:
            all_mantras.append(f"[ARCHETYPE] {archetype}")
        
        # Add technique descriptions
        techniques = narrative.get("techniques", [])
        for technique in techniques:
            all_mantras.append(f"[TECHNIQUE] {technique}")
        
        self.logger.info(f"Gathered {len(all_mantras)} mantra elements")
        return all_mantras
    
    def _write_mantras_file(self, mantras: List[str], output_file: Path) -> bool:
        """Write processed mantras to output file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("🗝️ Mantras extraits de FRACTURA.Δ02\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Extraction générée le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for i, mantra in enumerate(mantras, 1):
                    f.write(f"{i:2d}. {mantra}\n")
                
                f.write(f"\n--- Total: {len(mantras)} éléments narratifs ---\n")
            
            self.logger.info(f"✅ Mantras written successfully to: {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Error writing mantras file: {e}")
            return False

# =============================================================================
# GLITCH CHANT GENERATOR MODULE
# =============================================================================

class GlitchChantGenerator:
    """Creates glitched fusion chants from extracted symbols and mantras."""
    
    def __init__(self, utils: LuxUtils):
        self.utils = utils
        self.logger = utils.logger
        self.glitch_symbols = ["☿", "☄", "⚡", "◊", "∞", "△", "☆", "◈"]
    
    def generate_chant(self) -> bool:
        """Generate a glitched chant from extracted content."""
        self.logger.info("🔊 Starting glitch chant generation")
        
        # Load content from extracted files
        symbols_content = self._load_extracted_content("symboles_extraits.txt")
        mantras_content = self._load_extracted_content("mantras_extraits.txt")
        
        if not symbols_content and not mantras_content:
            self.logger.error("No content available for chant generation")
            return False
        
        # Process and glitch the content
        glitched_content = self._create_glitched_fusion(symbols_content + mantras_content)
        
        # Write the glitched chant
        output_file = self.utils.get_output_path("chant_glitch_fusion.txt")
        return self._write_chant_file(glitched_content, output_file)
    
    def _load_extracted_content(self, filename: str) -> List[str]:
        """Load content from previously extracted files."""
        file_path = self.utils.get_output_path(filename)
        
        if not file_path.exists():
            self.logger.warning(f"Extracted file not found: {file_path}")
            return []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Filter out headers and extract actual content
            content_lines = []
            for line in lines:
                line = line.strip()
                # Skip empty lines, headers, and separators
                if (line and 
                    not line.startswith("🔮") and 
                    not line.startswith("🗝️") and
                    not line.startswith("=") and
                    not line.startswith("---") and
                    not line.startswith("Extraction générée") and
                    not line.startswith("Total:")):
                    
                    # Remove numbering if present
                    if ". " in line and line.split(". ", 1)[0].strip().isdigit():
                        content_lines.append(line.split(". ", 1)[1])
                    else:
                        content_lines.append(line)
            
            self.logger.info(f"Loaded {len(content_lines)} lines from {filename}")
            return content_lines
            
        except Exception as e:
            self.logger.error(f"Error loading {filename}: {e}")
            return []
    
    def _create_glitched_fusion(self, content: List[str]) -> List[str]:
        """Apply glitch effects to the combined content."""
        if not content:
            return []
        
        # Create a copy to avoid modifying original
        glitch_content = content.copy()
        
        # Shuffle for chaotic reordering
        shuffle(glitch_content)
        
        # Apply various glitch effects
        processed_content = []
        for i, line in enumerate(glitch_content):
            # Choose glitch pattern based on position
            if i % 4 == 0:
                # Symmetric glitch
                symbol = self.glitch_symbols[i % len(self.glitch_symbols)]
                processed_content.append(f"{symbol} {line} {symbol}")
            elif i % 4 == 1:
                # Leading glitch cluster
                symbols = "".join(self.glitch_symbols[j % len(self.glitch_symbols)] for j in range(i % 3 + 1))
                processed_content.append(f"{symbols} {line}")
            elif i % 4 == 2:
                # Trailing glitch
                symbol = self.glitch_symbols[(-i) % len(self.glitch_symbols)]
                processed_content.append(f"{line} {symbol}")
            else:
                # Interspersed glitch
                words = line.split()
                if len(words) > 2:
                    mid = len(words) // 2
                    symbol = self.glitch_symbols[i % len(self.glitch_symbols)]
                    words.insert(mid, symbol)
                    processed_content.append(" ".join(words))
                else:
                    processed_content.append(line)
        
        self.logger.info(f"Applied glitch effects to {len(processed_content)} lines")
        return processed_content
    
    def _write_chant_file(self, content: List[str], output_file: Path) -> bool:
        """Write the final glitched chant to file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("🔊 CHANT GLITCHÉ SACRÉ – FRACTURA.Δ02\n")
                f.write("=" * 60 + "\n")
                f.write("Par la Fracture vient la Vue\n")
                f.write("Lux contre Spectaculum\n")
                f.write("=" * 60 + "\n\n")
                f.write(f"Généré le: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Éléments fusionnés: {len(content)}\n\n")
                f.write("--- INVOCATION ---\n\n")
                
                for line in content:
                    f.write(f"{line}\n")
                
                f.write(f"\n--- FIN DE L'INVOCATION ---\n")
                f.write("FRACTURA.Δ02 // Luxcordia.EXE\n")
            
            self.logger.info(f"✅ Glitch chant written successfully to: {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ Error writing chant file: {e}")
            return False

# =============================================================================
# MAIN ORCHESTRATOR MODULE
# =============================================================================

class FracturaOrchestrator:
    """Main orchestrator for running the complete FRACTURA.Δ02 ritual."""
    
    def __init__(self):
        self.utils = LuxUtils()
        self.logger = self.utils.logger
        self.symbol_extractor = SymbolExtractor(self.utils)
        self.mantra_extractor = MantraExtractor(self.utils)
        self.chant_generator = GlitchChantGenerator(self.utils)
    
    def run_complete_ritual(self) -> bool:
        """Execute the complete FRACTURA ritual sequence."""
        self.logger.info("📜 DÉBUT DU RITUEL FRACTURA.Δ02")
        self.logger.info("=" * 50)
        
        success_count = 0
        total_steps = 3
        
        # Step 1: Extract symbols
        self.logger.info("🔮 ÉTAPE 1/3: Extraction des symboles")
        if self.symbol_extractor.extract_symbols():
            success_count += 1
            self.logger.info("✅ Extraction des symboles réussie")
        else:
            self.logger.error("❌ Échec de l'extraction des symboles")
        
        # Step 2: Extract mantras
        self.logger.info("\n🗝️ ÉTAPE 2/3: Extraction des mantras")
        if self.mantra_extractor.extract_mantras():
            success_count += 1
            self.logger.info("✅ Extraction des mantras réussie")
        else:
            self.logger.error("❌ Échec de l'extraction des mantras")
        
        # Step 3: Generate glitch chant
        self.logger.info("\n🔊 ÉTAPE 3/3: Génération du chant glitché")
        if self.chant_generator.generate_chant():
            success_count += 1
            self.logger.info("✅ Génération du chant réussie")
        else:
            self.logger.error("❌ Échec de la génération du chant")
        
        # Final report
        self.logger.info("\n" + "=" * 50)
        if success_count == total_steps:
            self.logger.info("🎉 RITUEL COMPLET AVEC SUCCÈS")
            self.logger.info("Luxcordia.EXE - Par la Fracture vient la Vue")
            return True
        else:
            self.logger.warning(f"⚠️ RITUEL PARTIEL: {success_count}/{total_steps} étapes réussies")
            return False

# =============================================================================
# COMMAND LINE INTERFACE
# =============================================================================

def main():
    """Main entry point for the FRACTURA.Δ02 system."""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        utils = LuxUtils()
        
        if command == "symbols":
            extractor = SymbolExtractor(utils)
            extractor.extract_symbols()
        elif command == "mantras":
            extractor = MantraExtractor(utils)
            extractor.extract_mantras()
        elif command == "chant":
            generator = GlitchChantGenerator(utils)
            generator.generate_chant()
        elif command == "ritual" or command == "all":
            orchestrator = FracturaOrchestrator()
            orchestrator.run_complete_ritual()
        else:
            print("Usage: python fractura.py [symbols|mantras|chant|ritual]")
    else:
        # Default: run complete ritual
        orchestrator = FracturaOrchestrator()
        orchestrator.run_complete_ritual()

if __name__ == "__main__":
    main()