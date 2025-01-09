# Lesson 1.1: Creating and Importing Our Player
* before we begin coding in python/pygame, we must learn how the program is able to read animations

* pygame uses a **sprite sheet** - a single image that contains all the frames arranged in a row (it can also be in columns)

> <ins>Example</ins>: 
Let's say we have a character that can walk to the right. The walking animation would have 8 frames. In the **sprite sheet**, these frames would be arranged in a single row. Let's assume each frame is 64X64. This would mean the entire sheet would be 512x64 pixels (8 frames * the width of 64 pixels)

__Visual Example:__

![alt text](ImageFolder/user_walk.png)



> [!IMPORTANT] 
> Please take a look at classes V:1.0.0:

>[!NOTE] 
> To animate this in Pygame, we use a technique called "sprite sheet subsurface extraction"

```python
# Let's say our sprite sheet is loaded as an image
sprite_sheet = pygame.image.load("character_walk.png")

# Each frame is 64x64 pixels
frame_width = 64
frame_height = 64

# To get frame 3 (0-based index) from the first row:
frame_x = 3 * frame_width  # 192 pixels from the left
frame_y = 0  # First row starts at 0
frame_3 = sprite_sheet.subsurface((frame_x, frame_y, frame_width, frame_height))

```

### WHY USE SPRITE SHEETS?
1. <ins>Memory efficiency</ins> - loading one image is faster than loading many seperate files
2. <ins>Organization</ins> - all the related animations are kept together
3. <ins>Performance</ins> - Switching between frames is very quickly since the whole sheet is already in memory

* when creating your own games, you will typically have a simple system to track which frame you are on and when to move to the next one

```Python
    class Player:
        def __init__(self):
            self.sprite_sheet = pygame.image.load("user_walk.png")
            self.current_frame = 0
            self.animation_speed = 0.1 # seconds per frame
            self.animation_timer = 0
        def update(self, dt): # dt is delta time (seconds since last frame)
            # Update animation timer
            self.animation_timer += dt
            if self.animation_timer >= self.animation_speed:
            # move to the next frame
            self.current_frame = (self.current_frame + 1) % 8 # assuming 8 frames
            self.animation_timer = 0
```



