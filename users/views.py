from rest_framework.response import Response

from users.models import Place, UserCheckedInPlace, UserFollow

'''
Views contains the pseudo-codes of the APIs/methods required for the user location applications to work.

NB: Authentication and follow request accepting part is ignored. 
'''


def current_place(request):
    '''
    :param request: user current location (point field)
    :return: Places near the user location

    User provides the current location and places in that location will be returned as response
    '''
    try:
        # getting user location
        location = request.data.get('location')
        # listing places near user(polygon that contains the user locations)
        places = Place.objects.filter(location__intersects=location)  # ----> queryset need to be serialized

        return Response(
            {
                'success': True,
                'message': 'Successfully fetched places near user location',
                'data': places,
            }
        )
    except Exception as e:
        raise e


def user_checkin(request):
    '''
    :param request: user selects a place and the inputs the place id
    :return: Check in response, if success.
    '''
    try:
        # authenticated user
        user = request.user
        # the place id
        place = request.data.get('place')
        # creating user checkin data
        UserCheckedInPlace.objects.create(user=user, place_id=place)

        return Response(
            {
                'success': True,
                'message': 'Successfully fetched places near user location',
                'data': '',
            }
        )
    except Exception as e:
        raise e


def follow_user(request):
    '''
    :param request: the authenticated user provides the user id to be FOLLOWED
    :return: Success/failure response
    '''
    try:
        # authenticated user
        user = request.user
        # user id of user to be followed
        to_follow = request.data.get('to_follow')

        # checking whether request user is following the user to be followed
        if user.following.filter(following=to_follow).exists():
            # creating the following data based on user request
            UserFollow.objects.create(user=user, following=to_follow)

            return Response(
                {
                    'success': True,
                    'message': f'Successfully followed {to_follow}',
                    'data': '',
                }
            )
        else:
            return Response(
                {
                    'success': False,
                    'message': f'You are already following {to_follow}',
                    'data': '',
                }
            )
    except Exception as e:
        raise e


def unfollow_user(request):
    '''
    :param request: the authenticated user provides the user id to be UNFOLLOWED
    :return: Success/failure response
    '''
    try:
        # authenticated user
        user = request.user
        # user id of user to be unfollowed
        to_unfollow = request.data.get('to_follow')

        # checking whether request user is following the user to be unfollowed
        if user.following.filter(following=to_unfollow).exists():
            # removing the following data from DB
            UserFollow.objects.get(user=user, following=to_unfollow).delete()
            return Response(
                {
                    'success': True,
                    'message': f'Successfully unfollowed {to_unfollow}',
                    'data': '',
                }
            )
        else:
            return Response(
                {
                    'success': True,
                    'message': f'You are not following {to_unfollow}',
                    'data': '',
                }
            )
    except Exception as e:
        raise e


def user_following_list(request):
    '''
    :return: list of all users whom the request user is following
    '''
    try:
        # authenticated user
        user = request.user
        # list of all followed users
        following_list = user.following.all()  # ----> queryset need to be serialized
        return Response(
            {
                'success': True,
                'message': f'Successfully fetched following user list',
                'data': following_list,
            }
        )
    except Exception as e:
        raise e


def user_checked_in_location(request):
    '''
    :return: the list of locations a particular user had checked-in
    '''
    try:
        # authenticated user
        user = request.user
        # the id of user whose checked-in locations has to be retrieved
        searched_user = request.data.get('searched_user')

        # checking whether the request user is following the searched user
        if user.following.filter(following=searched_user).exists():
            # filtering the checked-in locations of searched user
            user_locations = UserCheckedInPlace.objects.filter(
                user_id=searched_user)  # ----> queryset need to be serialized
            return Response(
                {
                    'success': True,
                    'message': f'Successfully fetched user checked-in locations',
                    'data': user_locations,
                }
            )
        # Failure response if the request user is not following the searched user
        return Response(
            {
                'success': False,
                'message': f'You cannot view the locations of user whom you are not following',
                'data': '',
            }
        )
    except Exception as e:
        raise e
