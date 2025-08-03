import random
import time

class QuantumTradingSystem:
    def __init__(self, initial_balance=10000.0):
        self.balance = initial_balance
        self.portfolio = {}
        self.transaction_history = []
        self.current_price = {
            'ETH/USDT': 3500.0,
            'BTC/USDT': 60000.0,
            'SOL/USDT': 150.0,
            'DOT/USDT': 7.0
        }
        self.quantum_confidence = 0.5
        self.market_regime = 'SIDEWAYS'

    def _simulate_market_data(self):
        # Simulate changing market data based on the Flutter app's logic
        for asset in self.current_price:
            # Price fluctuation
            self.current_price[asset] *= (1 + (0.01 * (random.randint(0, 2) - 1)))
            self.current_price[asset] = round(self.current_price[asset], 2)

        # Quantum Confidence simulation
        self.quantum_confidence = round(0.7 + 0.1 * (random.randint(0, 9) / 10), 2)

        # Market Regime simulation
        second = int(time.time()) % 60
        if second < 20:
            self.market_regime = 'BULLISH'
        elif second < 40:
            self.market_regime = 'SIDEWAYS'
        else:
            self.market_regime = 'BEARISH'

        print(f"Market Update: Prices={self.current_price}, Confidence={self.quantum_confidence}, Regime={self.market_regime}")

    def execute_trade(self, action, asset, amount):
        if asset not in self.current_price:
            print(f"Error: Asset {asset} not supported.")
            return False

        cost = amount * self.current_price[asset]

        if action == 'BUY':
            if self.balance < cost:
                print("Error: Insufficient funds.")
                return False
            self.balance -= cost
            self.portfolio[asset] = self.portfolio.get(asset, 0) + amount
            print(f"BUY: {amount} of {asset} at {self.current_price[asset]}. Cost: {cost}. New Balance: {self.balance}")
        elif action == 'SELL':
            if self.portfolio.get(asset, 0) < amount:
                print("Error: Insufficient asset to sell.")
                return False
            self.balance += cost
            self.portfolio[asset] -= amount
            if self.portfolio[asset] == 0:
                del self.portfolio[asset]
            print(f"SELL: {amount} of {asset} at {self.current_price[asset]}. Revenue: {cost}. New Balance: {self.balance}")
        else:
            print("Error: Invalid action. Use 'BUY' or 'SELL'.")
            return False

        self.transaction_history.append({
            'action': action,
            'asset': asset,
            'amount': amount,
            'price': self.current_price[asset],
            'total': cost,
            'timestamp': time.time(),
            'confidence': self.quantum_confidence
        })
        return True

    def get_status(self):
        return {
            'balance': self.balance,
            'portfolio': self.portfolio,
            'current_prices': self.current_price,
            'quantum_confidence': self.quantum_confidence,
            'market_regime': self.market_regime,
            'transaction_history': self.transaction_history
        }

if __name__ == "__main__":
    system = QuantumTradingSystem()
    print("Initial Status:", system.get_status())

    # Simulate some market data updates
    for _ in range(3):
        system._simulate_market_data()
        time.sleep(1) # Simulate time passing

    # Execute some trades
    system.execute_trade('BUY', 'ETH/USDT', 0.1)
    system.execute_trade('BUY', 'BTC/USDT', 0.01)
    system.execute_trade('SELL', 'ETH/USDT', 0.05)

    print("\nFinal Status:", system.get_status())
    print("\nTransaction History:")
    for tx in system.transaction_history:
        print(tx)


