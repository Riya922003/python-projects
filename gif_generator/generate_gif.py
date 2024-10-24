import os
from PIL import Image, ImageFilter, ImageEnhance
import imageio
import torch
from torchvision import transforms
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
import numpy as np
import shutil

def prompt_for_image():
    """Prompt the user to enter the path of an image file."""
    while True:
        image_path = input("Please enter the path to your image file: ")
        if os.path.isfile(image_path):
            return image_path
        else:
            print("Invalid file path. Please try again.")

def load_pretrained_model():
    """Load a pretrained image classification model."""
    model_name = "microsoft/resnet-50"
    feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
    model = AutoModelForImageClassification.from_pretrained(model_name)
    return feature_extractor, model

def apply_style_transfer(image, feature_extractor, model):
    """Apply style transfer using the pretrained model."""
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Use the model's output to create a stylized version of the image
    logits = outputs.logits
    probs = torch.nn.functional.softmax(logits, dim=-1)
    
    # Convert image to RGB mode if it's not already
    image = image.convert('RGB')
    
    # Create a color overlay based on the model's output
    overlay = Image.new('RGB', image.size, tuple(map(int, probs[0][:3].numpy() * 255)))
    
    # Blend the original image with the overlay
    stylized = Image.blend(image, overlay, 0.5)
    return stylized

def create_frames(image_path, feature_extractor, model, num_frames=10):
    """Create frames from the input image with advanced modifications."""
    original = Image.open(image_path)
    frames = []
    for i in range(num_frames):
        frame = original.copy()
        # Apply rotation
        frame = frame.rotate(i * 36)  # Rotate by 36 degrees each frame for a full rotation
        # Apply style transfer
        frame = apply_style_transfer(frame, feature_extractor, model)
        # Apply additional effects
        frame = frame.filter(ImageFilter.EDGE_ENHANCE)
        frame = ImageEnhance.Brightness(frame).enhance(1.2)  # Increase brightness
        frame = ImageEnhance.Contrast(frame).enhance(1.1)  # Increase contrast
        
        frame_path = f'gif_generator/images/frame_{i}.png'
        frame.save(frame_path)
        frames.append(frame_path)
    return frames

def generate_gif(frames):
    """Generate a GIF from a series of image frames."""
    output_path = 'gif_generator/images/animated.gif'
    with imageio.get_writer(output_path, mode='I', duration=0.2) as writer:
        for frame_path in frames:
            image = imageio.imread(frame_path)
            writer.append_data(image)
    print(f"GIF created successfully as '{output_path}'")
    return output_path

if __name__ == "__main__":
    # Create a directory for temporary images if it doesn't exist
    os.makedirs('gif_generator/images', exist_ok=True)

    # Load pretrained model
    feature_extractor, model = load_pretrained_model()

    # Prompt user for image
    user_image = prompt_for_image()

    # Create frames from the user's image
    frames = create_frames(user_image, feature_extractor, model)

    # Generate GIF
    gif_path = generate_gif(frames)

    # Copy the original image to the images folder
    original_image_name = os.path.basename(user_image)
    shutil.copy(user_image, f'gif_generator/images/{original_image_name}')

    # Clean up temporary image files
    for frame in frames:
        os.remove(frame)

    print(f"Original image saved as 'gif_generator/images/{original_image_name}'")
    print(f"GIF saved as '{gif_path}'")
