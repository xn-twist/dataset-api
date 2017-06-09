# Enables available operations for resources/collections (defaults to ['GET'])
RESOURCE_METHODS = ['GET', 'POST']

# Enable available operations for individual items (defaults to ['GET'])
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

PUBLIC_METHODS = ['GET']

# ~~ ADMINS SCHEMA: Define the administrators of the system
admin_schema = {
    'username': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 12,
        'required': True,
        'unique': True,
    },
    'password': {
        'type': 'string',
        'minlength': 6,
        'maxlength': 32,
        'required': True,
    }
}

admins = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'public_methods': [],

    'schema': admin_schema
}
# ~~ END ADMINS SCHEMA ~~

# ~~ MAPPINGS SCHEMA: Mappings between latin chars and potential spoof chars
mappings_schema = {
    'character': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
        'unique': True,
    },
    'potential_spoofs': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'spoof_character': {'type': 'string'},
                'votes': {'type': 'integer'}
            }
        },
    }
}

mappings = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'character'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'public_methods': ["GET"],

    'schema': mappings_schema
}
# ~~ END MAPPINGS SCHEMA ~~

# ~~ FEED SCHEMA: A feed of the recently identified mappings
feed_schema = {
    'character': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
    },
    'spoof': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
    }
}

feed = {
    'item_title': 'feed',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'public_methods': ["GET", "POST"],
    'schema': feed_schema
}
# ~~ END FEED SCHEMA ~~

# ~~ BASIC LATIN CHARACTERS SCHEMA: Basic latin chars (a-z and 0-9)
basic_latin_characters_schema = {
    'basic_character': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
        'unique': True,
    }
}

basic_latin_characters = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'basic_character'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'public_methods': ["GET"],
    'schema': basic_latin_characters_schema
}
# ~~ END BASIC LATIN CHARACTERS SCHEMA ~~

# ~~ NON-BASIC CHARACTERS SCHEMA: chars that may be used to spoof basic chars
non_basic_characters_schema = {
    'potential_spoof': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
        'unique': True,
    }
}

non_basic_characters = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'potential_spoof'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'public_methods': ["GET"],
    'schema': non_basic_characters_schema
}
# ~~ END NON-BASIC CHARACTERS SCHEMA ~~

# ~~ SUGGESTED DEPRECATION FEED SCHEMA: chars suggested for deprecation
suggested_deprecations_feed_schema = {
    'character': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
        'unique': False,
    }
}

suggested_deprecations_feed = {
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'public_methods': ["GET", "POST"],
    'schema': suggested_deprecations_feed_schema
}
# ~~ END SUGGESTED DEPRECATION FEED SCHEMA ~~

# ~~ UNMAPPED CHARACTER FEED SCHEMA: chars to which no basic char. was mapped
unmapped_character_feed_schema = {
    'unmapped_character': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
        'unique': False,
    }
}

unmapped_character_feed = {
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'public_methods': ["GET", "POST"],
    'schema': unmapped_character_feed_schema
}
# ~~ END UNMAPPED CHARACTER FEED SCHEMA ~~

# ~~ DEPRICATED CHARACTERS SCHEMA: Chars that have been removed from the set
# of non_basic_chars
depricated_characters_schema = {
    'depricated_character': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
        'unique': True,
    }
}

depricated_characters = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'depricated_character'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'public_methods': ["GET"],
    'schema': depricated_characters_schema
}
# ~~ END DEPRICATED CHARACTERS SCHEMA ~~

# map each of the schemas above to a branch of the API
DOMAIN = {
    'administrators': admins,
    'mappings': mappings,
    'basic_characters': basic_latin_characters,
    'feed': feed,
    'non_basic_characters': non_basic_characters,
    'suggested_deprecations': suggested_deprecations_feed,
    'unmapped_characters': unmapped_character_feed,
    'depricated_characters': depricated_characters
}

# provide details for mongo instance
MONGO_HOST = 'localhost'
MONGO_PORT = 27018
MONGO_DBNAME = 'data'

# uncomment these to enforce rate limits on the API (uses REDIS)
# RATE_LIMIT_GET = (1, 30)
# RATE_LIMIT_POST = (1, 30)

# turn off pagination
PAGINATION = False

# add configurations that allow the API to be access remotely
X_DOMAINS = '*'
X_HEADERS = ['Origin', 'X-Requested-With', 'Content-Type', 'Accept',
             'If-Match']
