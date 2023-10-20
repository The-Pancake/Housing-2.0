//import React from 'react';
import { useLocation, Outlet, useNavigate } from 'react-router-dom';
import React, { useState, useEffect } from 'react';
import { profileData, hasMissingInformation } from './edit_contact_info.jsx';
import './styles.css';


//import {last_name} from './edit_contact_info.jsx';
//import {first_name} from './edit_contact_info.jsx';

//import { profileData, hasMissingInformation } from './edit_contact_info.jsx';


export default function Application() {
    const location = useLocation();
    const navigate = useNavigate();
    const currentStep = 3;
    const totalSteps = 5;
    const loadingPercentage = (currentStep / totalSteps) * 100;
    const [showMissingInfoPopup, setShowMissingInfoPopup] = useState(false);

    useEffect(() => {
        setShowMissingInfoPopup(hasMissingInformation(profileData));
    }, []);

    const handleEditInfoClick = () => {
        navigate('/edit-profile');
    };

    return (
        <>
            {showMissingInfoPopup && (
                <div className="missing-info-popup">
                    Missing information in profile, 
                    <span className="popup-link" onClick={handleEditInfoClick}> click here</span> to finish profile.
                </div>
            )}

            <div className="user-name">
                {profileData.lastName}, {' '}{profileData.firstName}
            </div>
            <div className="info-container">
                <div className="info-box personal-info-box">
                    <div className="box-header">Personal Information</div>
                    <div className="personal-info">Email: {profileData.email}</div>
                    <div className="personal-info">Class: {profileData.class}</div>
                    <div className="personal-info RIN-info">RIN: {profileData.RIN}</div>
                    <button className="edit-info-button" onClick={handleEditInfoClick}>
                        Edit Other Information 
                    </button>
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
            <Outlet />  {/* This will render the nested routes */}
        </>
    );
}
