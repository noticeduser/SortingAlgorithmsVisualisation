from PIL import Image

def split_image_into_quadrants(image_path, output_path, num_rows, num_columns):
    # Open the image
    original_image = Image.open(image_path)

    # Get the size of the original image
    original_width, original_height = original_image.size

    # Calculate the size of each quadrant
    quadrant_width = original_width // num_columns
    quadrant_height = original_height // num_rows

    # Loop through each row
    for row in range(num_rows):
        # Loop through each column
        for col in range(num_columns):
            # Calculate the coordinates of the current quadrant
            left = col * quadrant_width
            upper = row * quadrant_height
            right = left + quadrant_width
            lower = upper + quadrant_height

            # Crop the quadrant from the original image
            quadrant = original_image.crop((left, upper, right, lower))

            # Save the quadrant to the output path
            quadrant.save(f"{output_path}/quadrant_{row}_{col}.png")

if __name__ == "__main__":
    # Specify the input image path
    input_image_path = "C:/Users/Culle/Desktop/assets/joeyy.jpg"

    # Specify the output path where the quadrants will be saved
    output_path = "C:/Users/Culle/Desktop/assets/saved_quadrants"

    # Specify the number of rows and columns in the grid
    num_rows = 4
    num_columns = 4

    # Call the function to split the image into quadrants
    split_image_into_quadrants(input_image_path, output_path, num_rows, num_columns)
