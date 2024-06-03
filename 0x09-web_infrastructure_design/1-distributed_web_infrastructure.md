### Diagram

![[Infrastructure Diagram](https://i.postimg.cc/RZ6DVc8m/Two-s.avif)

### Components

1. **Load Balancer (HAProxy)**:
   - Distributes incoming traffic across multiple servers.
   - Round Robin.

2. **Web Server (Nginx)**:
   - Handles HTTP requests, serves static content, and forwards dynamic requests.

3. **Application Server**:
   - Processes dynamic content and handles application logic.

4. **Database (MySQL)**:
   - Handles write operations.
   - Handles read operations.

### Explanation

1. **User Request**: The user accesses `www.foobar.com`.
2. **DNS Resolution**: The domain resolves to the load balancer IP.
3. **Load Balancer (HAProxy)**: Forwards the request using the Round Robin algorithm.
4. **Web Server (Nginx)**: 
   - Handles static and dynamic content requests.
5. **Application Server**:
   - Processes requests and interacts with the database.
6. **Database Interaction**:
   - Manages write operations.
   - Manages read operations.

### Issues with This Infrastructure

1. **SPOF**:
   - Load Balancer: Failure causes system downtime.
   - Primary Database: Failure disrupts write operations.

2. **Security Issues**:
   - No firewall: Vulnerable to unauthorized access.
   - No HTTPS: Data transfer is not encrypted.

3. **No Monitoring**:
   - Lack of monitoring tools impacts performance and availability.
