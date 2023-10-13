import React from 'react';
import './styles.css';

export default function EditProfile() {
  const profileData = {
    firstName: 'John',
    lastName: 'Doe',
    dob: '1990-01-01',
    address: '123 Fake St, Imaginary City, 12345',
    phone: '+1 (518)-***-****',
    email: 'johndoe@example.com',
    gender: 'Male',
    pronouns: 'He/Him'
  };

  return (
    <div className="edit-profile-background">
      <div className="profile-container">
        <h1 className="profile-title">Edit Profile</h1>
        <div className="profile-section">
          <span className="profile-label">First Name:</span> {profileData.firstName}
        </div>
        <div className="profile-section">
          <span className="profile-label">Last Name:</span> {profileData.lastName}
        </div>
        <div className="profile-section">
          <span className="profile-label">Date of Birth:</span> {profileData.dob}
        </div>
        <div className="profile-section">
          <span className="profile-label">Address:</span> {profileData.address}
        </div>
        <div className="profile-section">
          <span className="profile-label">Phone:</span> {profileData.phone}
        </div>
        <div className="profile-section">
          <span className="profile-label">Email:</span> {profileData.email}
        </div>
        <div className="profile-section">
          <span className="profile-label">Gender:</span> {profileData.gender}
        </div>
        <div className="profile-section">
          <span className="profile-label">Pronouns:</span> {profileData.pronouns}
        </div>
        
        <div className="button-group">
          <button className="profile-edit-button">Edit Details</button>
          <button className="profile-save-changes-button">Save Changes</button>
        </div>
      </div>
    </div>
  );
}
