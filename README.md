# Bikelock

Smart Bike Lock - Embedded HCI Project Plan
Project Overview
Design and build an IoT-enabled bike lock that combines robust security with intuitive user experience, targeting the Swedish cycling market.
Core Features
Security & Hardware

Electronic locking mechanism with servo motor or solenoid
GPS tracking with cellular/WiFi connectivity
Accelerometer/gyroscope for movement detection
Battery management with solar charging capability
Weather-resistant housing (IP67 rating for Swedish weather)
Backup mechanical key for emergency access

Smart Connectivity

AWS IoT Core integration for device management
Mobile app (iOS/Android) for primary interface
Web dashboard for fleet management (bike sharing companies)
Bluetooth Low Energy for proximity unlocking
4G/LTE connectivity for remote monitoring

User Experience Features

Proximity unlock - automatically unlocks when owner approaches
Multiple unlock methods: smartphone app, PIN code, NFC tag, emergency key
Theft alerts with immediate push notifications
Location sharing with trusted contacts
Battery status monitoring with low-power warnings
Usage analytics (time locked, locations, trip data)

HCI Design Challenges
Mobile App Interface
Key Screens:
├── Lock/Unlock (primary action)
├── Location Map (current bike position)
├── Security Status (alerts, battery, connection)
├── Settings (unlock methods, notifications, sharing)
├── History (lock/unlock events, locations)
└── Emergency (lost phone access, emergency contacts)
Physical Interface Design

LED status indicators (locked/unlocked/battery/connectivity)
Physical keypad as backup (weatherproof, tactile feedback)
Audio feedback for confirmation (volume adjustable)
Haptic feedback through app when near lock

Accessibility Considerations

Voice commands through smartphone
High contrast LED colors for visibility
Large, tactile buttons on physical keypad
Screen reader compatibility in mobile app
Multiple authentication methods for different abilities

Technical Architecture
Hardware Components

Microcontroller: ESP32 (WiFi/Bluetooth integrated)
Cellular module: SIM7600 (4G connectivity)
GPS module: NEO-8M
IMU sensor: MPU6050 (motion detection)
Locking mechanism: High-torque servo or electromagnetic lock
Power: 18650 lithium battery + small solar panel
Security: Hardware encryption chip (ATECC608A)

Software Stack

Device firmware: FreeRTOS on ESP32
Cloud backend: AWS IoT Core + Lambda + DynamoDB
Mobile app: React Native (cross-platform)
Web dashboard: React + AWS Amplify
Communication: MQTT over TLS

AWS Services Integration

IoT Core: Device shadows, message routing
Lambda: Business logic, notifications
DynamoDB: User data, device history
SNS: Push notifications
Cognito: User authentication
API Gateway: Mobile app backend
CloudWatch: Monitoring and alerts

Security Features
Anti-Theft Measures

Tamper detection - accelerometer monitors unauthorized movement
Cut sensor - detects attempts to cut the lock cable
Silent alarm mode - tracks thief without alerting them
Fake shutdown - appears offline but continues tracking
Encrypted communication - all data transmission secured

Privacy Protection

Local data encryption on device
User consent for location sharing
Data retention policies (automatic deletion after time period)
Anonymous usage analytics option

User Research & Testing
Target User Groups

Daily commuters (convenience focus)
Casual cyclists (simplicity focus)
Bike sharing companies (fleet management focus)
Security-conscious users (anti-theft focus)

Usability Testing Scenarios

First-time setup process
Emergency unlock when phone is dead
Theft response - what happens when bike is stolen
Battery management - charging habits and warnings
Weather resilience - functionality in Swedish winter

User Journey Mapping
Typical Use Flow:
1. Approach bike → Proximity detection → Auto-unlock notification
2. Manual unlock via app → Visual/haptic confirmation
3. Ride bike → Location tracking (optional)
4. Park bike → Lock via app or auto-lock after timeout
5. Leave → Movement alerts if tampered with
Swedish Market Considerations
Local Requirements

Winter resilience - operates in -20°C temperatures
Swedbank integration - popular payment method for bike sharing
GDPR compliance - EU privacy regulations
Swedish language support in app interface
Integration with Göteborg/Stockholm bike sharing systems

Cultural Factors

Minimalist design - matches Swedish design preferences
Environmental consciousness - solar charging, recyclable materials
Trust-based society - balance security with convenience
Tech adoption - high smartphone usage, comfort with IoT devices

Development Phases
Phase 1: Core Functionality (8 weeks)

Basic lock/unlock mechanism
Mobile app with essential features
AWS IoT integration
GPS tracking

Phase 2: Enhanced Security (6 weeks)

Anti-theft features
Tamper detection
Advanced encryption
Emergency protocols

Phase 3: User Experience (6 weeks)

Proximity unlocking
UI/UX refinement
Accessibility features
User testing and iteration

Phase 4: Market Readiness (4 weeks)

Weather testing
Battery optimization
Swedish localization
Documentation and deployment

Expected Outcomes
Technical Deliverables

Functional prototype hardware
Complete mobile application
Web-based management dashboard
AWS cloud infrastructure
Security testing report

HCI Contributions

User research findings
Accessibility design patterns
Cross-cultural UX considerations
IoT interaction paradigms

Portfolio Value

Demonstrates full-stack IoT development
Shows understanding of security vs usability trade-offs
Proves ability to design for diverse user needs
Highlights market research and localization skills

Potential Industry Applications

Bike sharing companies (Tier, Lime, local Swedish companies)
Insurance companies (theft prevention, usage-based pricing)
Smart city initiatives (Uppsala, Stockholm mobility projects)
Consumer electronics (direct-to-consumer smart lock market)

This project perfectly positions you for internships at companies working on IoT, automotive interfaces, or smart city solutions in Sweden.
