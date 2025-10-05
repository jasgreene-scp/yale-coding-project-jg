# yale-coding-project-jg

I spent approximately 30 hours working on this as API's were relatively new to me. I was able to get my backend working and had I had a little more time, a day or so, I would have been able to get my front end working to display the correct plots/information.  The current selection available in my dropdowns were also just some hardcoed placeholders.

(not applicatble since front end is not currently communicating with backend in my code)⚠️ Queries may take a bit to run due to full dataset size (100k) and cohort logic. This is expected behavior. Optimazation efforts may be applied at a later time to fix latency issues.

OMOP tables utilized:
I used the concept-ID mapping table provided to be able to get the drop down options for the disease selector. This also gets utilized to determine the disease counts for disease versus non-disease after being selected from the dropdown in the UI.
I used the meassurement table to get the sex distribution informtion and age distribution information in relevance to the selected disease.
I used the condition occurence table to check if any specific person had or didn't have the disease within the cohort.
I used the person table to get information such as birth date, age, and sex for the comparison plots.

AI Utilized: Microsoft Copilot
Since I have never used DuckDB or built a cohort before, I used AI to give me some direction as to how to do it. I additionally do not have a lot of experience with API's, I also had AI help me with that as well.
The main prompts I gave are listed below, and I additionally asked clarifying questions which would be a little too much to list here:

1. "How can I use DuckDB to implement cohort construction using OMOP tables?"
2. "I would like to pull data from aws S3 buckets to utilize in cohort creation using DuckDB"
3. "What is the suggested folder structure based on the assignment I am trying to do" and I gave it a general summary of the backend and front end information, and some specifics directly from the document
4. I generally consulted AI on how to do a lot of code formatting as well, especially with api routes, as well as correct error handling.
