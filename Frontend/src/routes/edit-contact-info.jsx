import React from 'react';
import './styles.css';



export const profileData = {
  firstName: 'Jeremy',
  lastName: 'Lin',
  class: 'Junior',
  dob: '1990-01-01',
  address: '12345 Alfredo St, Savannah, GA, 45469',
  streetAddress: '12345 Alfredo Ave',
  city: 'Savannah',
  state: 'GA',
  country: 'United States',
  zipcode: '45649',
  phone: '+1(518)-999-9999',
  RIN: '666666666',
  email: 'doejo2@rpi.edu',
  gender: 'Male',
  pronouns: 'He/Him'
};


const mandatoryFields = ['firstName', 'lastName', 'RIN', 'email'];

export function hasMissingInformation(data) {
  const keysToCheck = [
    'firstName', 'lastName', 'class', 'dob', 'streetAddress', 
    'city', 'state', 'country', 'zipcode', 'phone', 
    'RIN', 'email', 'gender', 'pronouns'
  ];
  
  for (let key of keysToCheck) {
    if (!data[key] || data[key].trim() === '') {
      return true;
    }
  }
  return false;
}

export function hasMandatoryMissing(data) {
  for (let field of mandatoryFields) {
    if (!data[field] || data[field].trim() === '') {
      return true;
    }
  }
  return false;
}



export default function EditProfile() {
  return (
    <div className="edit-profile-background">
      <div className="profile-container">
        <h1 className="profile-title">Edit Profile</h1>

        {/* First and Last Name */}
        <div className="row">
          <div className="profile-section half">
            <span className="profile-label"><span className="mandatory-field">*</span>First Name:</span> 
            {profileData.firstName}
          </div>
          <div className="profile-section half">
            <span className="profile-label"><span className="mandatory-field">*</span>Last Name:</span> 
            {profileData.lastName}
          </div>
        </div>

        {/* RIN, Class, Email */}
        <div className="row">
          <div className="profile-section third">
            <span className="profile-label"><span className="mandatory-field">*</span>RIN:</span> 
            {profileData.RIN}
          </div>
          <div className="profile-section third">
            <span className="profile-label"><span className="mandatory-field">*</span>Class:</span>
            {profileData.class}
          </div>
          <div className="profile-section third">
            <span className="profile-label"><span className="mandatory-field">*</span>Email:</span> 
            {profileData.email}
          </div>
        </div>

        {/* Date of Birth */}
        <div className="row">
          <div className="profile-section full">
            <span className="profile-label">Date of Birth:</span> 
            {profileData.dob}
          </div>
        </div>

        {/* Address Details */}
        <div className="row">
          <div className="profile-section third">
            <span className="profile-label">Street Address:</span> 
            {profileData.streetAddress}
          </div>
          <div className="profile-section third">
            <span className="profile-label">City:</span> 
            {profileData.city}
          </div>
          <div className="profile-section third">
            <span className="profile-label">State:</span> 
            {profileData.state}
          </div>
        </div>

        {/* Country, Zipcode, Phone */}
        <div className="row">
          <div className="profile-section third">
            <span className="profile-label">Country:</span> 
            {profileData.country}
          </div>
          <div className="profile-section third">
            <span className="profile-label">Zipcode:</span> 
            {profileData.zipcode}
          </div>
          <div className="profile-section third">
            <span className="profile-label">Phone:</span> 
            {profileData.phone}
          </div>
        </div>

        {/* Gender and Pronouns */}
        <div className="row">
          <div className="profile-section half">
            <span className="profile-label">Gender:</span> 
            {profileData.gender}
          </div>
          <div className="profile-section half">
            <span className="profile-label">Pronouns:</span> 
            {profileData.pronouns}
          </div>
        </div>

        {/* Buttons */}
        <div className="button-group">
          <button className="profile-edit-button">Edit Details</button>
          <button className="profile-save-changes-button">Save Changes</button>
        </div>
      </div>
    </div>
  );
}

