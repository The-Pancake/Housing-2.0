import React, { ChangeEvent, FormEvent, useState } from "react";

const DormImageForm = () => {
    const [image, setImage] = useState<File | null>(null);

    const handleImageChange = (e: ChangeEvent<HTMLInputElement>) => {
        const selectedImage = e.target.files?.[0];
        setImage(selectedImage || null);
    };

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        // You can handle image submission logic here, e.g., upload to a server
        if (image) {
            // Submit image to server
            console.log("Submitting image:", image);
        } else {
            // Handle error for no image selected
            console.error("No image selected");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="imageInput">Upload Dorm Image</label>
                <input
                    type="file"
                    className="form-control-file"
                    id="imageInput"
                    accept="image/*"
                    onChange={handleImageChange}
                />
                <small className="form-text text-muted">
                    Accepted file formats: JPG, PNG, GIF
                </small>
            </div>
            <button type="submit" className="btn btn-primary">
                Submit
            </button>
        </form>
    );
};

export default DormImageForm;
