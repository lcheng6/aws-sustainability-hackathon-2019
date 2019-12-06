import React, { useState, useEffect } from 'react'
import Statement from './statement'
import Visualisation from './visualisation'
import { Row, Col } from 'antd'
import { Layout } from 'antd';

const { Header, Footer, Sider, Content } = Layout;

const Page = () => {

    const [hasError, setErrors] = useState(false);
    const [footballFields, setFootballFields] = useState({});

    useEffect(() => {
        async function fetchData() {
            const res = await fetch("https://xu52io6cpl.execute-api.us-east-1.amazonaws.com/test/deforestation?location=Brazil&month=January");
            res
                .json()
                .then(res => setFootballFields(res))
                .catch(err => setErrors(err));
        }

        fetchData();
    });

    return <div>
        <Layout>
            <Header><h1>The scale of deforestation</h1></Header>
            <Content>
                <Row>
                    <Col><Statement /></Col>
                </Row>
                <Row>
                    <Col><Visualisation /></Col>
                </Row>
                <Row>
                    <p>{footballFields.footballFields}</p>
                </Row>
            </Content>

        </Layout>
    </div>
}

export default Page;