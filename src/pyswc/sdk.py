import requests as requests_http
from .general import General
#from .membership import Membership
#from .player import Player
#from .scoring import Scoring
from .sdkconfiguration import SDKConfiguration
from pyswc.utils import utils
from pyswc.utils import retries
from typing import Dict

class Swcapi:
    r"""Sports World Central (SWC) Fantasy Football API:
    This API provides read-only access to info from the Sports World Central (SWC) Fantasy Football API. 🏈. 
    The endpoints are grouped into the following categories:

    ## Player
    You can get a list of an NFL players, or search for an individual player by player_id.

    ## Scoring
    You can get a list of NFL player performances, including the fantasy points they scored using SWC league scoring.

    ## Membership
    Get information about all the SWC fantasy football leagues and the teams in them.
    """
    general: General
    #player: Player
    # scoring: Scoring
    # membership: Membership

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: retries.RetryConfig = None
                 #retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, None, server_url, server_idx, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.general = General(self.sdk_configuration)
        #self.player = Player(self.sdk_configuration)
        # self.scoring = Scoring(self.sdk_configuration)
        # self.membership = Membership(self.sdk_configuration)
    