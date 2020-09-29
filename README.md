# SPARK LOCATIONS

The Spark Locations is a Django Application that let users follow one another. Any user the can view the locations that a user(whom he/she is following) had checked-in.

## Models

- Place:
    - Store the global data og places.
    - The table will be prepopulated with places around the globe(so that the user can get the list of places based on their location).
    - Places are stored as the 'PolygonField' using the Django GIS.
- User:
    - User table contains the basic user data such as the username, first_name, last_name, email.
- UserCheckedInPlace:
    - This table contains the details of places that the user had checked-in.
    - 'places' field represents the foreign key of place table.
- UserFollowing:
    - This table contains the details user following and followers

## Views(Pseudo-codes/methods)
- **_'current_place'_**:
    - This method contains the pseudo-code user current place.
    - The user will be providing the current location(point field).
    - The places near the user current location will be fetched based the user location and the list will be returned.
- **_'user_checkin'_**:
    - This method creates the user check-in data.
    - User will be selecting a place_id from the list provided based on the location.
- **_'follow_user'_**:
    - This method creates user following data if the requested is not following the a particular user.
- **_'unfollow_user'_**:
    - This method removes user following data if it exists for the requested user and a particular user.
- **_'user_following_list'_**:
    - This method retrieves the list of all users whom the requested user is following.
- **_'user_checked_in_places'_**:
    - Retrieves the list of places a particular user had checked-in.
    - The requested user will provide a user_id as input and the list of all places the user had checked-in will be retrieved if only the request user is following that particular uer.
