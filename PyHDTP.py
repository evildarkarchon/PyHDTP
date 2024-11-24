import argparse
import subprocess
import sys
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Texture Pack File Management Script")

    parser.add_argument("--base-path", type=str, default=str(Path.cwd()), required=True, help="Base path where all texture folders are located")

    parser.add_argument("--combined-dir", type=str, default=str(Path.cwd() / "Combined_Files"), help="Name of the output directory (default: Combined_Files)")

    parser.add_argument("--skip-confirm", action="store_true", help="Skip confirmation prompts")

    return parser.parse_args()


def pause(skip_confirm: bool = False) -> None:
    if not skip_confirm:
        input("Press Enter to continue...")


def print_separator() -> None:
    print("\n" + "=" * 80 + "\n")


def delete_files(base_path: Path, file_paths: list[Path]) -> None:
    """Delete files if they exist."""
    for file_path in file_paths:
        full_path = base_path / file_path
        try:
            if full_path.exists():
                full_path.unlink()
                print(f"Deleted: {full_path}")
        except FileNotFoundError as e:
            print(f"Error deleting {full_path}: {e}")


def robocopy_folder(source_path: Path, dest_path: Path) -> None:
    """Execute robocopy command for the specified folders."""
    print(f"\nCopying files from {source_path.name} to {dest_path.name}...")

    try:
        result = subprocess.run(["robocopy", str(source_path), str(dest_path), "/s"], check=False, capture_output=True, text=True)

        # Robocopy has special return codes
        if result.returncode > 7:  # 8 or higher indicates an error
            print(f"Warning: Robocopy reported issues:\n{result.stderr}")
        else:
            print("Copy operation complete.\n")

    except Exception as e:
        print(f"Error during copy operation: {e}\n")
        raise


def validate_paths(args: argparse.Namespace) -> tuple[Path, Path]:
    """Validate that all required paths exist."""
    base_path = Path(args.base_path)
    if not base_path.exists():
        raise FileNotFoundError(f"Base path does not exist: {base_path}")

    # Check required subdirectories
    required_dirs = ["01_FlaconOil", "02_Langley", "03_Valius", "04_NMC", "05_Lucid", "06_TilesRubble01", "07_Other"]

    missing_dirs = [dir_name for dir_name in required_dirs if not (base_path / dir_name).exists()]

    if missing_dirs:
        raise FileNotFoundError(f"Missing required directories: {', '.join(missing_dirs)}")

    # Create combined directory if it doesn't exist
    combined_path = Path(args.combined_dir)
    combined_path.mkdir(exist_ok=True)

    return base_path, combined_path


def main() -> None:
    args = parse_arguments()

    try:
        base_path, combined_path = validate_paths(args)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Using base path: {base_path}")
    print(f"Output directory: {combined_path}")
    pause(args.skip_confirm)

    print("\nExtract the mods to the 5 folders as per the instructions BEFORE running this script.")
    pause(args.skip_confirm)

    # Process FlaconOil files
    print("\nProcessing FlaconOil's Complete Retexture Project...")
    robocopy_folder(base_path / "01_FlaconOil", combined_path)

    # Define conflicting files (relative to base path)
    flacon_conflicting = [
        Path(r"01_FalconOil\textures\setdressing\office\OfficeBoxPapers01_Clean_d.dds"),
        Path(r"01_FalconOil\textures\setdressing\office\OfficeBoxPapers01_Clean_n.dds"),
        Path(r"01_FalconOil\textures\setdressing\office\OfficeBoxPapers01_d.dds"),
        Path(r"01_FalconOil\textures\setdressing\office\OfficeBoxPapers01_n.dds"),
        Path(r"01_FalconOil\textures\setdressing\Tires\Tires01_d.DDS"),
        Path(r"01_FalconOil\textures\setdressing\Tires\Tires01_n.DDS"),
        Path(r"01_FalconOil\textures\setdressing\Tires\Tires01_s.DDS"),
        Path(r"01_FalconOil\textures\architecture\buildings\ResWindowSheet_d.DDS"),
        Path(r"01_FalconOil\textures\architecture\buildings\ResWindowSheet_n.DDS"),
        Path(r"01_FalconOil\textures\architecture\buildings\ResWindowSheet_s.DDS"),
        Path(r"01_FalconOil\textures\architecture\DiamondCity\corrugatedmetal05_n.dds"),
        Path(r"01_FalconOil\materials\architecture\DiamondCity\corrugatedmetal05.bgsm"),
        Path(r"01_FalconOil\materials\architecture\DiamondCity\corrugatedmetal05alpha.bgsm"),
    ]

    langley_conflicting = [
        Path(r"02_Langley\textures\architecture\buildings\Bricks01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01Painted01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01Painted01_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01R_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01R_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01R_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01Trim_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01Trim_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks01Trim_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks02_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks02R_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Bricks02Trim_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksDarkRed01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksFactory01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksFactory01R_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksGreen01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksGreen01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksGS01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksGS01_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksRed01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksWhite01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksWhite01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BricksWhite01R_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BrickTrim01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BrickTrim01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BrickTrim01_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BrickWhite02Win01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\BrickWhite02Win01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Debris01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Debris01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Debris01_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Debris02_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Plaster01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Plaster01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Plaster01_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Plaster02_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Plaster02_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\Plaster02_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\ResAwningFabric01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\ResAwningFabric01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\ResAwningFabric01_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\ResAwningFabric02_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\resawningfabric03_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\resawningfabric03_s.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\ResAwningFabric04_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\WoodFloor01_d.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\WoodFloor01_n.DDS"),
        Path(r"02_Langley\textures\architecture\buildings\WoodFloor01_s.DDS"),
        Path(r"02_Langley\textures\interiors\building\bldwoodfloor01_d.dds"),
        Path(r"02_Langley\textures\interiors\building\bldwoodfloor01_n.dds"),
        Path(r"02_Langley\textures\interiors\building\bldwoodfloor01_s.dds"),
        Path(r"02_Langley\textures\SetDressing\WoodFederalistFurniture01_d.DDS"),
        Path(r"02_Langley\textures\SetDressing\WoodFederalistFurniture01_n.DDS"),
        Path(r"02_Langley\textures\SetDressing\WoodFederalistFurniture01_s.DDS"),
        Path(r"02_Langley\materials\architecture\buildings\BrickBrownstone01.bgsm"),
        Path(r"02_Langley\materials\architecture\buildings\BrickBrownstonePainted01.bgsm"),
        Path(r"02_Langley\materials\architecture\buildings\BrickBrownstonePainted02.bgsm"),
        Path(r"02_Langley\materials\architecture\buildings\BrickGreenLt01.bgsm"),
        Path(r"02_Langley\materials\architecture\buildings\BrickRed01.BGSM"),
        Path(r"02_Langley\materials\architecture\buildings\BrickRedDamageDecal01.BGSM"),
        Path(r"02_Langley\materials\architecture\buildings\BricksFactory01.BGSM"),
        Path(r"02_Langley\materials\architecture\buildings\BrickSolidWhitePaint01.bgsm"),
        Path(r"02_Langley\materials\architecture\buildings\BrickTan01.BGSM"),
        Path(r"02_Langley\materials\architecture\buildings\BrickTanLt01.bgsm"),
    ]

    print("\nDeleting conflicting FlaconOil files...")
    delete_files(base_path, flacon_conflicting)

    print("\nDeleting conflicting Langley files...")
    delete_files(base_path, langley_conflicting)

    # Process remaining texture packs
    folders = [
        ("01_FlaconOil", "FlaconOil's Complete Retexture Project"),
        ("02_Langley", "Langley's HD Textures Workshop"),
        ("03_Valius", "High Resolution Texture Pack 2K and 4K - Valius"),
        ("04_NMC", "NMC's Texture Bundle"),
        ("05_Lucid", "Lucid's Texture Upgrades"),
        ("06_TilesRubble01", "SavrenX TilesRubble01"),
        ("07_Other", "Other"),
    ]

    for folder, description in folders:
        print(f"\nProcessing {description}...")
        robocopy_folder(base_path / folder, combined_path)

    print_separator()
    print(f"4estGimp - HDTP has completed copying files to the {args.combined_dir} folder.")
    print("Ready to create archive files.")
    print_separator()

    print("\nAll files have been successfully combined.")
    print("You can now proceed with creating the BA2 archives.")
    print("\nThank You")
    print("\nPress Enter to exit...")
    input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"\nFile not found error: {e}")
        print("Please check the paths and try again.")
        input("\nPress Enter to exit...")
        sys.exit(1)
    except PermissionError as e:
        print(f"\nPermission error: {e}")
        print("Please check your permissions and try again.")
        input("\nPress Enter to exit...")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"\nSubprocess error: {e}")
        print("There was an error with a subprocess call.")
        input("\nPress Enter to exit...")
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print(f"\nAn unexpected error occurred: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)
