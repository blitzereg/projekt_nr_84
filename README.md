# Embedding GitHub Pages Content in Squarespace

This guide explains how to embed interactive content hosted on GitHub Pages into a Squarespace page. 
Follow these steps to display interactive content like charts or visualizations on your Squarespace website.

## Steps to Embed Interactive Content

1. **Log in to your Squarespace account** and go to the page editor where you want to embed the content.
2. **Add a new block** by clicking on the **"Add Block"** button.
3. **Choose the "Code" block** from the available block options.
4. **Paste the following code** into the Code block editor:


    ```html
    <iframe width="100%" height="500px" 
            src="https://blitzereg.github.io/projekt_nr_84/127.0.0.1.html" 
            frameborder="0">
    </iframe>
    ```

    > **Note**: Make sure to use correct URL.

5. **Save and publish** the changes to your page.
6. Your interactive content will now be embedded in the Squarespace page, and users will be able to interact with it directly.

---

## Troubleshooting

If the iframe doesn't display your content:

1. Double-check the URL path in the `src` field.
2. Make sure the URL you are using is publicly accessible and not hosted locally.
3. Ensure your GitHub Pages site is live and properly configured.

---

By following these steps, you can easily embed content from GitHub Pages into your Squarespace website. 
If you need more help with the process, feel free to reach out!
