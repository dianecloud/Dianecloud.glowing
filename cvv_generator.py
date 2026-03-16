import sys
import random

def generate_cvv(digits: int = 3) -> str:
    """
    Generates a random CVV (Card Verification Value).
    - Visa/Mastercard: 3 digits (000-999)
    - American Express: 4 digits (0000-9999)
    """
    if digits not in (3, 4):
        raise ValueError("CVV length must be 3 or 4 digits")
    return ''.join(str(random.randint(0, 9)) for _ in range(digits))

def main() -> None:
    # Command-line interface (run from CMD/PowerShell/Terminal)
    # Usage examples:
    #   python cvv_generator.py          → 1 × 3-digit CVV
    #   python cvv_generator.py 10       → 10 × 3-digit CVVs
    #   python cvv_generator.py 5 4      → 5 × 4-digit CVVs (Amex style)
    
    args = sys.argv[1:]
    
    try:
        count = int(args[0]) if args else 1
        length = int(args[1]) if len(args) > 1 else 3
    except (ValueError, IndexError):
        print("Usage: python cvv_generator.py [count] [length=3|4]")
        print("Example: python cvv_generator.py 20 3")
        sys.exit(1)
    
    if count < 1 or length not in (3, 4):
        print("Error: count must be ≥1, length must be 3 or 4")
        sys.exit(1)
    
    print(f"Generating {count} CVV{'s' if count > 1 else ''} ({length} digits):\n")
    for i in range(count):
        cvv = generate_cvv(length)
        print(f"  {i+1:2d}. {cvv}")

if __name__ == "__main__":
    main()

  # uses diane.cloud@mail.com
