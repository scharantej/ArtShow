## Flask Application Design for an Art Gallery with Sample Images

### HTML Files

**index.html**
- Main HTML file for the gallery.
- Contains the page's layout, including header, footer, and image display area.
- Should include styling to enhance the visual appeal of the gallery.

**image_detail.html**
- Displays detailed information about a specific image, such as its title, artist, and description.
- Also provides a larger view of the image.

### Routes

**@app.route('/')**
- Root route that displays the main gallery page (index.html).

**@app.route('/image/<int:image_id>')**
- Displays detailed information about an image with the specified image_id (image_detail.html).

**@app.route('/images')**
- Provides an API endpoint to fetch a list of all images in the gallery. This endpoint can be useful for populating the gallery on the front end.