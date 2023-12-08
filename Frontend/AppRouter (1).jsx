import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Application from './application';
import EditProfile from './edit_contact_info';

function AppRouter() {
    return (
        <Routes>
            <Route path="/" element={<Application />} />
            <Route path="/edit-profile" element={<EditProfile />} />
        </Routes>
    );
}

export default AppRouter;
