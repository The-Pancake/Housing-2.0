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
  phone: '+1 (518)-999-9999',
  RIN: '666666666',
  email: 'doejo2@rpi.edu',
  gender: 'Male',
  pronouns: 'He/Him'
};

export default function EditProfile() {
  return (
    <div className="edit-profile-background">
      <div className="profile-container">
        <h1 className="profile-title">Edit Profile</h1>

        <div className="row">
          <div className="profile-section">
            <span className="profile-label">First Name:</span> {profileData.firstName}
          </div>
          <div className="profile-section">
            <span className="profile-label">Last Name:</span> {profileData.lastName}
          </div>
        </div>

        <div className="row">
          <div className="profile-section">
            <span className="profile-label">RIN:</span> {profileData.RIN}
          </div>
          <div className="profile-section">
            <span className="profile-label">Email:</span> {profileData.email}
          </div>
          <div className="profile-section">
            <span className="profile-label">Class:</span> {profileData.class}
          </div>
        </div>


        <div className="row">
          <div className="profile-section">
            <span className="profile-label">Date of Birth:</span> {profileData.dob}
          </div>
        </div>

        <div className="row">
          <div className="profile-section">
            <span className="profile-label">Street Address:</span> {profileData.streetAddress}
          </div>
          <div className="profile-section">
            <span className="profile-label">City:</span> {profileData.city}
          </div>
          <div className="profile-section">
            <span className="profile-label">State:</span> {profileData.state}
          </div>
        </div>

        <div className="row">
          <div className="profile-section">
            <span className="profile-label">Country:</span> {profileData.country}
          </div>
          <div className="profile-section">
            <span className="profile-label">Zipcode:</span> {profileData.zipcode}
          </div>
        </div>

        <div className="row">
          <div className="profile-section">
            <span className="profile-label">Phone:</span> {profileData.phone}
          </div>
        </div>

        <div className="row">
          <div className="profile-section">
            <span className="profile-label">Gender:</span> {profileData.gender}
          </div>
          <div className="profile-section">
            <span className="profile-label">Pronouns:</span> {profileData.pronouns}
          </div>
        </div>

        <div className="button-group">
          <button className="profile-edit-button">Edit Details</button>
          <button className="profile-save-changes-button">Save Changes</button>
        </div>
      </div>
    </div>
  );
}
