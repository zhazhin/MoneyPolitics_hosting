from os.path import dirname, abspath
import gettext as _

DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
USE_I18N = True

#  from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': ""
}

SESSION_CONFIGS = [
    {
        'name': 'MoneyPolitics',
        'display_name': 'Base Code MoneyPolitics',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "tax_rate",
        # Cost per message
        'msg': float(2),
        # The number of messages: 'none', 'single' or 'double'
        'msg_type': 'single',
        'suggested_parameter': False, # if true, participants suggest a parameter alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MoneyPoliticsTest',
        'display_name': 'MoneyPolitics (Test with 2 players)',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 2, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "tax_rate",
        # Cost per message
        'msg': float(2),
        # The number of messages, 'single' or 'double'
        'msg_type': 'single',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris, Diamonds, SumNDigit
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MP_Prog_Free_Cost_x_Single_MSG',
        'display_name': 'MoneyPolitics-Progressivity with Free Single Messaging',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "progressivity",
        # Cost per message
        'msg': float(0),
        # The number of messages, 'single' or 'double'
        'msg_type': 'single',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MP_Prog_Free_Cost_x_Dual_MSG',
        'display_name': 'MoneyPolitics-Progressivity with Free Dual Messaging',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "progressivity",
        # Cost per message
        'msg': float(0),
        # The number of messages, 'single' or 'double'
        'msg_type': 'double',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MP_Prog_2point_Cost_x_Single_MSG',
        'display_name': 'MoneyPolitics-Progressivity with 2 Point Cost Single Messaging',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "progressivity",
        # Cost per message
        'msg': float(2),
        # The number of messages, 'single' or 'double'
        'msg_type': 'single',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MP_Prog_2point_Cost_x_Dual_MSG',
        'display_name': 'MoneyPolitics-Progressivity with 2 Point Cost Dual Messaging',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "progressivity",
        # Cost per message
        'msg': float(2),
        # The number of messages, 'single' or 'double'
        'msg_type': 'double',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MP_Free_Cost_x_Single_MSG',
        'display_name': 'MoneyPolitics with Free Single Messaging',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "tax_rate",
        # Cost per message
        'msg': float(0),
        # The number of messages, 'single' or 'double'
        'msg_type': 'single',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MP_Free_Cost_x_Double_MSG',
        'display_name': 'MoneyPolitics with Free Dual Messaging',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "tax_rate",
        # Cost per message
        'msg': float(0),
        # The number of messages, 'single' or 'double'
        'msg_type': 'double',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MP_2Point_Cost_x_Single_MSG',
        'display_name': 'MoneyPolitics with 2 Point Cost Single Messaging',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "tax_rate",
        # Cost per message
        'msg': float(2),
        # The number of messages, 'single' or 'double'
        'msg_type': 'single',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
    {
        'name': 'MP_2Point_x_Double_MSG',
        'display_name': 'MoneyPolitics with 2 Point Cost Dual Messaging',
        #Set to 2 for demo but will be 9 for actual testing
        'num_demo_participants': 9, #Constants.players_per_group must also be changed in models.py
        'app_sequence': ['MoneyPolitics'],
        # Which tax system is going to be used (tax_rate or progressivity)
        'tax_system': "tax_rate",
        # Cost per message
        'msg': float(2),
        # The number of messages, 'single' or 'double'
        'msg_type': 'double',
        'suggested_parameter': True, # if true, participants suggest a tax alongside the msg
        "matching": 'fixed', # matching system for  particints (fixed: same as first round, random: random per round )
        'prob_of_luck': [0, 40], # probability of players endowment being assigned by luck. List that takes values from 0 to 100
        'payoffs_db': "payoffs.csv", # relative path to payoffs
        'effort_on_practice': True,
        'real_effort_task': "Diamonds", # Tetris or Diamonds
        'msg_order': 'low-high', #low-high, #high-low, #random
        'exclusive_senders': [], # list with endowments of players who can message. Empty for letting everyone msg
        'reveal_votes': True, # reveal votes if true
    },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
POINTS_DECIMAL_PLACES = 1
USE_POINTS = True


ROOMS = [
    {
        'name': 'EconoLab',
        'display_name': 'Laboratorio de Economía',
        'participant_label_file': '_rooms/econolab.txt',
    },
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
#ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '^sj1@)7g$9!w19h=jyd0sdqof@uwo2f^_d-zy9ra!rg!rf!ku*'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

LOCALE_PATHS = (
    SITE_ROOT + '/locale',
)