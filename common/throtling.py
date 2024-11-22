from rest_framework.throttling import SimpleRateThrottle, UserRateThrottle


class CreateUserContactApplicationPhoneThrottle(SimpleRateThrottle):
    rate = '3/h'
    scope = 'create_user_contact_application'

    def get_cache_key(self, request, view):
        return request.data.get('phone')


class CreateUserContactApplicationIPThrottle(UserRateThrottle):
    rate = '2/m'
    scope = 'create_user_contact_application'