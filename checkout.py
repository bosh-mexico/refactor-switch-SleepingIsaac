from enum import Enum

# Define Payment Modes
class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3
    UNKNOWN = 99

# Handlers for each payment mode
def process_paypal(amount: float):
    print(f"Processing PayPal payment of ${amount:.2f}")
    # Add PayPal-specific logic here

def process_googlepay(amount: float):
    print(f"Processing GooglePay payment of ${amount:.2f}")
    # Add GooglePay-specific logic here

def process_creditcard(amount: float):
    print(f"Processing Credit Card payment of ${amount:.2f}")
    # Add Credit Card-specific logic here

# Dispatch table mapping enum -> handler
PAYMENT_HANDLERS = {
    PaymentMode.PAYPAL: process_paypal,
    PaymentMode.GOOGLEPAY: process_googlepay,
    PaymentMode.CREDITCARD: process_creditcard,
}

# Checkout function
def checkout(mode: PaymentMode, amount: float):
    handler = PAYMENT_HANDLERS.get(mode)
    if handler:
        handler(amount)
    else:
        print("Invalid payment mode selected!")

# Example usage
if __name__ == "__main__":
    amount = 150.75

    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)
