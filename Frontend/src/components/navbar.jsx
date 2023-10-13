import { Link } from "react-router-dom";

import "./navbar.css"

export default function Navbar() {
  const routes = [
    {
      path: "",
      name: "index"
    },
    {
      path: "dorms",
      name: "dorms"
    },
    {
      path: "account",
      name: "account info"
    },
    {
      path: "contact",
      name: "contact us"
    },
    {
      path: "application",
      name: "profile and application"
    },
    {
      path: "signup",
      name: "signup page"
    }
  ];

  return (
    <ul id="navbar">
      <li className="logo">
        <Link to="">
          <h1>Housing 2.0</h1>
        </Link>
      </li>
      {routes.map((route) => {
        return (
          <li key={route.path}>
            <Link to={route.path}>{route.name}</Link>
          </li>
        );
      })}
    </ul>
  );
}