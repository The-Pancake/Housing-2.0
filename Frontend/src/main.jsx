import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import Root from "./routes/root";
import Dorms from "./routes/dorms";
import Account from "./routes/account";
import Contact from "./routes/contact";
import Application from "./routes/application";



const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
  },
  {
    path: "/dorms",
    element: <Dorms/>
  },
  {
    path: "/account",
    element: <Account/>
  },
  {
    path: "/contact",
    element: <Contact/>
  },
  {
    path: "/application",
    element: <Application/>
  }

]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);