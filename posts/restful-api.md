<!--
.. title: RESTful API
.. slug: restful-api
.. date: 2020-01-26 17:57:59 UTC-08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->



- REST = Representational State Transfer

- "REST is, in a nutshell, HTTP commands pushing JSON packets over the network."
    - This is not really true but a lot of people get by with this understanding.
    - HTTP and JSON not actually required to be REST
- understanding HTTP and being able to work with the response data (usually JSON or XML) seems to be more important for using API than actually understanding REST architectural constraints. 
- restful api example:  https://pokeapi.co/
- REST's Architectural Constraints
    - client-server
    - stateless
        - servers don't maintain any client state
        - No client data is stored on the server between requests and session state is stored on the client
        - If the client application needs to be a stateful application for the end-user, where user logs in once and do other authorized operations after that, then each request from the client should contain all the information necessary to service the request – including authentication and authorization details.
    - cacheable
        - servers must mark their responses as cacheable or not. So, infrastructures and clients can cache them when possible to improve performance.
    - uniform interface
        - the resource representations across the system should follow specific guidelines such as naming conventions, link formats, or data format (XML or/and JSON).
    - layered system
        - REST allows you to use a layered system architecture where you deploy the APIs on server A, and store data on server B and authenticate requests in Server C, for example. A client cannot ordinarily tell whether it is connected directly to the end server, or to an intermediary along the way.
