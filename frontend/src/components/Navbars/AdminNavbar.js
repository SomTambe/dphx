/*!

=========================================================
* Black Dashboard PRO React - v1.2.0
=========================================================

* Product Page: https://www.creative-tim.com/product/black-dashboard-pro-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
// nodejs library that concatenates classes
import classNames from "classnames";

// reactstrap components
import {
  Row,
  Col,
} from "reactstrap";

const AdminNavbar = (props) => {
  const [collapseOpen, setCollapseOpen] = React.useState(false);
  const [modalSearch, setModalSearch] = React.useState(false);
  const [color, setColor] = React.useState("navbar-transparent");
  React.useEffect(() => {
    window.addEventListener("resize", updateColor);
    return function cleanup() {
      window.removeEventListener("resize", updateColor);
    };
  });
  // function that adds color white/transparent to the navbar on resize (this is for the collapse)
  const updateColor = () => {
    if (window.innerWidth < 993 && collapseOpen) {
      setColor("bg-white");
    } else {
      setColor("navbar-transparent");
    }
  };
  // this function opens and closes the collapse on small devices
  const toggleCollapse = () => {
    if (collapseOpen) {
      setColor("navbar-transparent");
    } else {
      setColor("bg-white");
    }
    setCollapseOpen(!collapseOpen);
  };
  // this function is to open the Search modal
  const toggleModalSearch = () => {
    setModalSearch(!modalSearch);
  };
  return (
    <>
      <div className="container" style={{ paddingTop: 25 }}>
        <Row>
          <Col xs="3">
            {/* <img src="IIT_Kanpur_Logo.svg" alt="logo" /> */}
          </Col>
          <Col xs="12">
            <blockquote className="blockquote text-center">
              <h1 className="m-0">Double Pipe Heat Exchanger</h1>
              {/* <h3 className="mb-0">
                SEC Filing Analyzer for SaaS Companies
              </h3> */}
            </blockquote>
          </Col>
          <Col xs="3"></Col>
          </Row>
      </div>
    </>
  );
};

export default AdminNavbar;
