from summoner.server import SummonerServer
from summoner.your_package import hello_summoner

if __name__ == "__main__":
    hello_summoner()
    SummonerServer(name="SummonerServer").run(config_path="server_config.json")
