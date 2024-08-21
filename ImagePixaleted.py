from PIL import Image
import numpy as np

def remove_background(image, threshold=(245, 245, 245), bg_color=(255, 255, 255)):
    # Convert the image to a numpy array
    img_array = np.array(image)
    
    # Create a mask where the color is similar to the threshold
    mask = np.all(img_array >= threshold, axis=-1)
    
    # Set the background pixels to the desired background color (e.g., white)
    img_array[mask] = bg_color
    
    return Image.fromarray(img_array)

def average_color(image, x, y, block_size):
    block = image[y:y+block_size, x:x+block_size]
    return block.mean(axis=(0, 1))

def process_image(input_image_path, output_image_path, block_size=32, threshold=(245, 245, 245), bg_color=(255, 255, 255)):
    # Load the image
    img = Image.open(input_image_path)
    img = img.convert('RGB')  # Ensure it's in RGB format
    
    # Remove the background
    img_no_bg = remove_background(img, threshold, bg_color)
    
    # Convert the image with no background to a numpy array
    img_array = np.array(img_no_bg)
    
    # Calculate the new image size
    new_width = img_array.shape[1] // block_size
    new_height = img_array.shape[0] // block_size
    
    # Create an array to store the average colors
    avg_colors = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    
    # Loop through the image and calculate average colors
    for y in range(0, img_array.shape[0], block_size):
        for x in range(0, img_array.shape[1], block_size):
            avg_color = average_color(img_array, x, y, block_size)
            avg_colors[y // block_size, x // block_size] = avg_color
    
    # Create a new image from the average colors
    new_img = Image.fromarray(avg_colors, 'RGB')
    new_img = new_img.resize((block_size * new_width, block_size * new_height), Image.NEAREST)
    
    # Save the processed image
    new_img.save(output_image_path)

# Example usage
process_image('image_[507]/2.jpeg', 'output_image.jpg', threshold=(245, 245, 245), bg_color=(255, 255, 255))
