# EC500C1 Building Software API Exercise 1
## Description
### Function of this Miniproject
This is an API exercise. In the exercise, the user can:
1. Download the first 15 pictures from a specific twitter account by tweepy API.
2. Transform the pictures into a video by FFMPEG API.
3. Extract characteristics of those pictures by Google Vision API and save them into a json file.

In the main python program file, you can change this part of code to adjust the video properties:

    os.system("ffmpeg -framerate 5 -pattern_type glob -i '*.jpg'     -c:v libx264 -r 30 -pix_fmt yuv420p production.mp4")
    
You can change the "5" to adjust the pictures you want to have in the video. And you can change the "30" to change the phrame of the video. And you can change the "producion.mp4" to change the video's name.
But there are some problems.

### Problems
1. Till now, this program can only combine ".jpg" format pictures into video. If some pictures in the twitter are ".png" format, they will not be included in the video.
2. If the change the video part's format from ".mp4" to other video format, such as ".avi", it still gonna work, but the showing speed of the video will be asymmetry.
3. The txt document produced contains only one picture's label, instead of all the pictures contained in the video.

# EC500C1 Building Software Database Exercise 
After using both of the two database tools to save the data of the world airport, I found that these two tools are different in these aspects:

1. We must connect the server before we can write, read, upload, delete data in the database by using mongoDB. In other words, we must connect the internet before using mongoDB. However, we can use MySQL off-line. We just need to install MySQL on computer, then we do not need to connect internet to use MySQL. We can write python code to create database on our own computer, instead of on the server side.

2. Since we can use MySQL off-line, it also means the databse may occupy more space on our own computer. The mongoDB only cost a little space on personal computer.

3. MySQL and mongoDB save date in different ways. When we use MySQL, we must state what format we want to input into the database. However, when we use mongoDB, we can input data in dictionary or hash table type.
