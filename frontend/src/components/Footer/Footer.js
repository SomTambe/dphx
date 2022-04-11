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
/*eslint-disable*/
import React from "react";
import { Col, Container, Row } from "reactstrap";
// used for making the prop types of this component
import PropTypes from "prop-types";
// import logo from 'IIT_Kanpur_Logo.svg';

const Footer = (props) => {
  return (
    <footer className={"footer" + (props.default ? " footer-default" : "")}>
      <Container fluid={props.fluid ? true : false}>
        <Row>
          <Col xs="3"></Col>
          <Col>
            <ul className="nav">
              <li className="nav-item">
                <h1>
                  Jeet Bindra Unit Operations & Innovation Lab
                </h1>
              </li>
            </ul>
          </Col>
        </Row>
        
        {/* <div className="copyright">
          Today, {new Date().getDate()}{"/"}{new Date().getMonth()}{"/"}{new Date().getFullYear()} made by{" "}
          <a target="_blank">
             Som V Tambe.
          </a>{" "}
        </div> */}
      </Container>
    </footer>
  );
};

Footer.propTypes = {
  default: PropTypes.bool,
  fluid: PropTypes.bool,
};

export default Footer;
