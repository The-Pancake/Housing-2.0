import React, { ChangeEvent, FormEvent, useState } from "react";

const DormReviewForm = () => {
    const [rating, setRating] = useState(0);
    const [comment, setComment] = useState("");

    const handleRatingChange = (e: ChangeEvent<HTMLInputElement>) => {
        const selectedRating = parseInt(e.target.value);
        setRating(selectedRating);
    };

    const handleCommentChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
        const selectedComment = e.target.value;
        setComment(selectedComment);
    };

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        // You can handle review submission logic here, e.g., submit to a server
        if (rating && comment) {
            // Submit review to server
            console.log("Submitting review:", { rating, comment });
        } else {
            // Handle error for incomplete review
            console.error("Incomplete review");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div className="form-group">
                <label htmlFor="ratingInput">Rating</label>
                <input
                    type="number"
                    className="form-control"
                    id="ratingInput"
                    min="1"
                    max="5"
                    value={rating}
                    onChange={handleRatingChange}
                />
            </div>
            <div className="form-group">
                <label htmlFor="commentInput">Comment</label>
                <textarea
                    className="form-control"
                    id="commentInput"
                    rows={4}
                    value={comment}
                    onChange={handleCommentChange}
                ></textarea>
            </div>
            <button type="submit" className="btn btn-primary">
                Submit
            </button>
        </form>
    );
};

export default DormReviewForm;
