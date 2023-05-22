from soft_dns_server import SoftDnsServer

if __name__ == "__main__":
    server = SoftDnsServer()
    try:
        server.run()
    except KeyboardInterrupt:
        sys.exit(0)