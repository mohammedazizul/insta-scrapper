# to load all instagram posts using username --------------------------------------------------------------------------------------
# import instaloader

# def get_post_text(username):
#     # Create an instance of Instaloader
#     loader = instaloader.Instaloader()

#     try:
#         # Retrieve the profile metadata
#         profile = instaloader.Profile.from_username(loader.context, username)

#         # Iterate over the posts and print their captions
#         for post in profile.get_posts():
#             print(post.caption)
#     except instaloader.exceptions.ProfileNotExistsException:
#         print(f"Profile with username '{username}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     username = "username"  # Specify the username here
#     get_post_text(username)


# to load 5 instagram posts using username --------------------------------------------------------------------------------------
# import instaloader

# def get_post_data_by_day(username, num_posts):
#     # Create an instance of Instaloader
#     loader = instaloader.Instaloader()

#     try:
#         # Retrieve the profile metadata
#         profile = instaloader.Profile.from_username(loader.context, username)

#         # Initialize a list to store post data
#         post_data = []

#         # Iterate over the posts and gather data
#         for post in profile.get_posts():
#             if post.caption is not None:
#                 post_date = post.date.strftime('%Y-%m-%d')

#                 # Extract image URL, caption, and post URL
#                 image_url = post.url
#                 caption = post.caption
#                 post_url = f"https://www.instagram.com/p/{post.shortcode}"

#                 # Create a dictionary for the post
#                 post_dict = {
#                     'date': post_date,
#                     'caption': caption,
#                     'imageUrl': image_url,
#                     'postUrl': post_url
#                 }
#                 post_data.append(post_dict)

#             # Break the loop if the desired number of posts is reached
#             if len(post_data) >= num_posts:
#                 break

#         # Print post data
#         for post in post_data:
#             print("____________________________________________________________________________")
#             print("date:", post['date'])
#             print("caption:", post['caption'])
#             print("imageUrl:", post['imageUrl'])
#             print("postUrl:", post['postUrl'])
#     except instaloader.exceptions.ProfileNotExistsException:
#         print(f"Profile with username '{username}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     username = "trykemy"  # Specify the username here
#     num_posts = 5  # Specify the number of posts to retrieve
#     get_post_data_by_day(username, num_posts)


# to load 5 instagram posts using username with certain details --------------------------------------------------------------------------------------
# import instaloader

# def print_post_attributes(post):
#     print("Available attributes for the post:")
#     for attr in dir(post):
#         if not attr.startswith('__'):
#             print(attr)

# def get_post_data_by_day(username, num_posts):
#     # Create an instance of Instaloader
#     loader = instaloader.Instaloader()

#     try:
#         # Retrieve the profile metadata
#         profile = instaloader.Profile.from_username(loader.context, username)
#         # print(profile)

#         # Initialize a list to store post data
#         post_data = []

#         # Iterate over the posts and gather data
#         for post in profile.get_posts():
#             if post.caption is not None:
#                 post_date = post.date.strftime('%Y-%m-%d')
                
#                 # print_post_attributes(post)

#                 # Extract image URL, caption, and post URL
#                 image_url = post.url
#                 caption = post.caption
#                 post_url = f"https://www.instagram.com/p/{post.shortcode}"

#                 # Extract additional information
#                 likes_count = post.likes
#                 comments_count = post.comments
#                 location = post.location
#                 post_type = post.typename
#                 user_info = {
#                     'username': post.owner_username,
#                     'follower_count': post.owner_profile.followers,
#                     'following_count': post.owner_profile.followees,
#                     'bio': post.owner_profile.biography,
#                     'is_private': post.owner_profile.is_private,
#                     'is_verified': post.owner_profile.is_verified
#                 }

#                 # Check if the post has tags
#                 if hasattr(post, 'tags'):
#                     tags = post.tags
#                 else:
#                     tags = []

#                 # Create a dictionary for the post
#                 post_dict = {
#                     'date': post_date,
#                     'caption': caption,
#                     'imageUrl': image_url,
#                     'postUrl': post_url,
#                     'likesCount': likes_count,
#                     'commentsCount': comments_count,
#                     'location': location,
#                     'tags': tags,
#                     'postType': post_type,
#                     'userInfo': user_info
#                 }
#                 post_data.append(post_dict)

#             # Break the loop if the desired number of posts is reached
#             if len(post_data) >= num_posts:
#                 break

#         # Print post data
#         for post in post_data:
#             print("......................................................................................................")
#             print("Date:", post['date'])
#             print("Caption:", post['caption'])
#             print("Image URL:", post['imageUrl'])
#             print("Post URL:", post['postUrl'])
#             print("Likes Count:", post['likesCount'])
#             print("Comments Count:", post['commentsCount'])
#             print("Location:", post['location'])
#             print("Tags:", post['tags'])
#             print("Post Type:", post['postType'])
#             print("User Information:")
#             print("\tUsername:", post['userInfo']['username'])
#             print("\tFollower Count:", post['userInfo']['follower_count'])
#             print("\tFollowing Count:", post['userInfo']['following_count'])
#             print("\tBio:", post['userInfo']['bio'])
#             print("\tPrivate Account:", post['userInfo']['is_private'])
#             print("\tVerified Account:", post['userInfo']['is_verified'])
#             print("......................................................................................................")
#     except instaloader.exceptions.ProfileNotExistsException:
#         print(f"Profile with username '{username}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     username = "trykemy"  # Specify the username here
#     num_posts = 1  # Specify the number of posts to retrieve
#     get_post_data_by_day(username, num_posts)


# to load 5 instagram posts using username with certain details and create json file --------------------------------------------------------------------------------------
# import instaloader
# import json

# def get_post_data_by_day(username, num_posts):
#     # Create an instance of Instaloader
#     loader = instaloader.Instaloader()

#     try:
#         # Retrieve the profile metadata
#         profile = instaloader.Profile.from_username(loader.context, username)

#         # Initialize a list to store post data
#         post_data = []

#         # Iterate over the posts and gather data
#         for post in profile.get_posts():
#             if post.caption is not None:
#                 post_date = post.date.strftime('%B %d, %Y')

#                 # Extract image URLs, caption, and post URL
#                 image_urls = [post.url]
#                 for node in post.get_sidecar_nodes():
#                     if node.is_video:
#                         continue
#                     image_urls.append(node.display_url)
                    
#                 caption = post.caption
#                 post_url = f"https://www.instagram.com/p/{post.shortcode}"
#                 insta_link = f"https://www.instagram.com/{username}/"

#                 # Create a dictionary for the post
#                 post_dict = {
#                     'caption': caption,
#                     'postPic': image_urls,
#                     'instaLink': insta_link,
#                     'postLink': post_url,
#                     'venueName': profile.full_name,
#                     'label': 1,
#                     'postDate': post_date
#                 }
#                 post_data.append(post_dict)

#             # Break the loop if the desired number of posts is reached
#             if len(post_data) >= num_posts:
#                 break

#         # Print post data as JSON
#         print(json.dumps(post_data, indent=4))
#     except instaloader.exceptions.ProfileNotExistsException:
#         print(f"Profile with username '{username}' does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     username = "shangrilakl"  # Specify the username here
#     num_posts = 1  # Specify the number of posts to retrieve
#     get_post_data_by_day(username, num_posts)


# to load certain number of instagram posts using username with certain details and save into json file --------------------------------------------------------------------------------------
import instaloader
import json

def get_post_data_by_day(username, num_posts, output_file):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Retrieve the profile metadata
        profile = instaloader.Profile.from_username(loader.context, username)

        # Initialize a list to store post data
        post_data = []

        # Iterate over the posts and gather data
        for post in profile.get_posts():
            if post.caption is not None:
                post_date = post.date.strftime('%B %d, %Y')

                # Extract image URLs, caption, and post URL
                image_urls = [post.url]
                for node in post.get_sidecar_nodes():
                    if node.is_video:
                        continue
                    image_urls.append(node.display_url)
                    
                caption = post.caption
                post_url = f"https://www.instagram.com/p/{post.shortcode}"
                insta_link = f"https://www.instagram.com/{username}/"

                # Create a dictionary for the post
                post_dict = {
                    'caption': caption,
                    'postPic': image_urls,
                    'instaLink': insta_link,
                    'postLink': post_url,
                    'venueName': profile.full_name,
                    'label': 1,
                    'postDate': post_date
                }
                post_data.append(post_dict)

            # Break the loop if the desired number of posts is reached
            if len(post_data) >= num_posts:
                break

        # Write post data to JSON file
        with open(output_file, 'w') as json_file:
            json.dump(post_data, json_file, indent=4)
            
        print(f"Post data saved to '{output_file}'")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username '{username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    username = "shangrilakl"  # Specify the username here
    num_posts = 1  # Specify the number of posts to retrieve
    output_file = "post_data.json"  # Specify the output file name
    get_post_data_by_day(username, num_posts, output_file)






