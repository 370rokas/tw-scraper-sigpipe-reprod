from tradingview_scraper.symbols.stream.price import RealTimeData
import threading, time

EXCHANGE_SYMBOLS = ["FOREXCOM:XAUUSD", "FOREXCOM:EURUSD", "FOREXCOM:GBPJPY"]

def process_packet(packet):
    print("Processing packet:", packet.get('m'))
    # Simulate the processing of the packet
    time.sleep(1)

if __name__ == "__main__":
    real_time_data = RealTimeData()
    data_generator = real_time_data.get_latest_trade_info(exchange_symbol=EXCHANGE_SYMBOLS)

    for packet in data_generator:
        # Send off the packet to be handled in a thread
        threading.Thread(target=process_packet, args=(packet,)).start()
