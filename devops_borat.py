from random import choice
from errbot import botcmd, BotPlugin
import twitter


consumer_key='7hQkMRDXkRcHxuVvfwYFcVh2v'
consumer_secret='mSOagAeJQN0EqZPyhP8e1SRwDVixKGNCgd5VXeYZ6k1IGnPyyY'
access_token_key='324841391-JT37mccobuIv185EoUf0Zl79SVxe7jW2fZpmmsk9'
access_token_secret='0dwFpqjVAH4MEzE1iDbEd6plrUUXaYM3CxJml98O6XDvA'


class TwitterApi(object):
	def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
		self.api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
		                       access_token_key=access_token_key, access_token_secret=access_token_secret)
		super(TwitterApi, self).__init__()

	def get_statuses_for(self, user_name):
		return self.api.GetUserTimeline(screen_name=user_name, count=200)


class DevOpsBorat(BotPlugin):
	"""
    Quotes from various dev humour related twitter accounts
    """

	def __init__(self):
		self.twitter = TwitterApi(consumer_key, consumer_secret, access_token_key, access_token_secret)
		super(DevOpsBorat, self).__init__()


	@botcmd
	def borat(self, mess, args):
		"""
        Random quotes from the DEVOPS_BORAT twitter account
        """
		values = self.twitter.get_statuses_for('DEVOPS_BORAT')
		return choice(values).text

	@botcmd
	def jesus(self, mess, args):
		"""
        Random quotes from the devops_jesus twitter account
        """
		values = self.twitter.get_statuses_for('devops_jesus')
		return choice(values).text

	@botcmd
	def yoda(self, mess, args):
		"""
        Random quotes from the UXYoda twitter account
        """
		values = self.twitter.get_statuses_for('UXYoda')
		return choice(values).text

