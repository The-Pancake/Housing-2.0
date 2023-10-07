import React from 'react';
import { useLocation } from 'react-router-dom';
import './styles.css';

export default function Application() {
    const location = useLocation();
    const firstName = "Firstname";
    const lastName = "Lastname";

    const currentStep = 3;
    const totalSteps = 5;
    const loadingPercentage = (currentStep / totalSteps) * 100;
    const student_email = "lastnf@rpi.edu";
    const student_phone_number = "+1 (518)-***-****";

    return (
        <>
            <div className="user-name">
                {lastName}, {' '}{firstName}
            </div>
            <div className="info-container">
                <div className="info-box personal-info-box">
                    <div className="box-header">Personal Information</div>
                    <div className="personal-info">Email: {student_email}</div>
                    <div className="personal-info phone-info">Phone: {student_phone_number}</div>
                    <button className="edit-info-button">Edit Contact Info</button>
                </div>
                <div className="info-box status-info-box">
                    <div className="box-header">Application Status</div>
                    <div className="loading-bar-container">
                        <div className="loading-bar" style={{ width: `${loadingPercentage}%` }}></div>
                        <div className="loading-text">{loadingPercentage}%</div>
                    </div>
                    <div className="step-info">Step: {currentStep}/{totalSteps}</div>
                    <button className="continue-application-button">Continue Application</button>
                </div>
            </div>
            <div className="path-info">Current path: {location.pathname}</div>
        </>
    );
}
