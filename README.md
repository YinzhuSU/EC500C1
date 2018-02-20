# EC500C1
Building Software

This is an API exercise. In the exercise, the user can:
1. Download the first 15 pictures from a specific twitter account by tweepy API.
2. Transform the pictures into a video by FFMPEG API.
3. Extract characteristics of those pictures by Google Vision API and save them into a json file.

In the main python program file, you can change this part of code to adjust the video properties:

    os.system("ffmpeg -framerate 5 -pattern_type glob -i '*.jpg'     -c:v libx264 -r 30 -pix_fmt yuv420p production.mp4")
    
You can change the "5" to adjust the pictures you want to have in the video. And you can change the "30" to change the phrame of the video. And you can change the "producion.mp4" to change the video's name.
But there are some problems.
1. Till now, this program can only combine ".jpg" format pictures into video. If some pictures in the twitter are ".png" format, they will not be included in the video.
2. I don't know if the program can produce videos of other format except ".mp4", such as ".rmvb".
