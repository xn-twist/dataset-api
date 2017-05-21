# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# ~~ MAPPINGS SCHEMA: Mappings between latin chars. and potential spoof chars.
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

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

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
    'resource_methods': ['GET', 'POST'],
    'schema': feed_schema
}
# ~~ END FEED SCHEMA ~~

# ~~ BASIC LATIN CHARACTERS SCHEMA: Basic latin chars. (a-z and 0-9)
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
    'resource_methods': ['GET', 'POST'],
    'schema': basic_latin_characters_schema
}
# ~~ END BASIC LATIN CHARACTERS SCHEMA ~~

# ~~ POTENTIAL SPOOFS SCHEMA: Chars. that may be used as spoofs of latin chars.
potential_spoofs_schema = {
    'potential_spoof': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1,
        'required': True,
        'unique': True,
    }
}

potential_spoofs = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'potential_spoof'
    },
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET', 'POST'],
    'schema': potential_spoofs_schema
}
# ~~ END POTENTIAL SPOOFS SCHEMA ~~

# map each of the schemas above to a branch of the API
DOMAIN = {
    'mappings': mappings,
    'basic_characters': basic_latin_characters,
    'feed': feed,
    'characters': potential_spoofs
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
