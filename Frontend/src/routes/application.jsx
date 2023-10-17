import React from 'react';
import { useLocation, Outlet, useNavigate } from 'react-router-dom';
import './styles.css';


//import {last_name} from './edit_contact_info.jsx';
//import {first_name} from './edit_contact_info.jsx';

import {profileData} from './edit_contact_info.jsx';

export default function Application() {
    const location = useLocation();
    const navigate = useNavigate();
    const currentStep = 3;
    const totalSteps = 5;
    const loadingPercentage = (currentStep / totalSteps) * 100;

    const handleEditInfoClick = () => {
        navigate('/edit-profile');
    };

    return (
        <>
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
                        Edit Other Contact Info
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
            <div className="path-info">Current path: {location.pathname}</div>
            <Outlet />  {/* This will render the nested routes */}
        </>
    );
}
