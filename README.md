GitHub repo: 

Project: Guild Member Hub
About: Guild is tech company that administers education and upskilling benefits to America's largest employers. We refer to our eligible populations as "members" and support them in continuing education and career growth by coordinating policies and payments with our members, their employers, and their learning providers. All members are working adults, and the vast majority of coursework is online.  In current state, there's no way for members to interact with each other. Additionaly, it can be difficult for members to know which of the three stakeholders (employer, learning partner, or Guild) is the best point of contact for certain questions.  This application is intended to provide a centralized space of resources as well as an opportunity to find community with other Guild members chasing their personal and professional dreams. 

Wireframe 
1.) Guild Support Central -- index.html -- is the member's resource hub, outlining three existing branches of support in their upskilling journey. They then have the option to log in/register for the Guild Member Hub to interact with the Guild member community. 
2.) Guild Member Hub login or registration -- login.html 
3.) Guild Member Hub homepage -- home.html -- is where the individual member is greeted by name and can viewe posts and achievements by other members. They can add a new post -- post.html -- or edit -- edit.html -- or delete their existing posts.  They can also navigate to the Guild Achievement Gallery. 
4.) Guild Achievement Gallery -- gallery.html -- is where members can browse photos of Guild members celebrating milestones in their education and upskilling journey

Features 
1.) Flask application connected to MySQL database
2.) User login and registration + validations
3.) User can access all posts, add a new post, and edit or delete their post(s)
4.) OOP using classmethods and staticmethods
5.) GET routes + validations 
6.) POST routes + validations 
7.) Session and logout 

Product Backlog
1.) Chatbot -- Guild has created numerous resources for their members, and a chatbot on the Guild Support Central page could be a 24/7 automated assistant in pointing them in the right direction
2.) "Like" and/or Comment feature -- in both the Guild Member Hub posts and the Guild Achievement Gallery, I'd like to see a space where users can interact in a "social media" sense; however, I know this is not a business need and raises several concerns of monitoring and acceptable use of the platform 
3.) File upload -- give user the option to upload a file instead of relying on existing media in the Guild Achievement Gallery
4.) Account verification -- to ensure only verified Guild members access the platform, they would use their existing Guild login information and/or SSO