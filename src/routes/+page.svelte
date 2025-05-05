<script lang="ts">
  function smoothScroll(node: HTMLAnchorElement) {
    const handleClick = (event: { preventDefault: () => void; }) => {
      event.preventDefault();
      
      const targetId = node.getAttribute('href')?.substring(1);
      
      if (!targetId) {
        console.warn('No target specified for smooth scroll');
        return;
      }
      
      const targetElement = document.getElementById(targetId);
      
      if (!targetElement) {
        console.error(`Target element with id "${targetId}" not found`);
        return;
      }
      
      targetElement.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
        inline: 'nearest'
      });
    };
    
    node.addEventListener('click', handleClick);
    
    return {
      destroy() {
        node.removeEventListener('click', handleClick);
      }
    };
  }
</script>
<header style="display: flex; align-items: center; justify-content: space-between; padding: 1rem; background-color: #e3f2fd; font-family:Anton, sans-serif; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    <h1 style="font-size: 2rem; color: rgba(227, 242, 253, 0.9); margin: 0;">
        <div style="display: flex; align-items: center; gap: 0.5rem">
            <a href="https://www.flaticon.com/free-icons/nemo" title="nemo icons">
            <img src="/fishing-net.png" alt="Fishing Net" style="width: 48px; height: 48px;"/>
            </a>
            <span>Net Gains</span>
        </div>
    </h1>
    <nav>
        <div style="display: flex; gap: 1rem;"> 
            <a href="#home" use:smoothScroll style="text-decoration: none; color: rgba(227, 242, 253, 0.9);">Home</a>
            <a href="#research_qs" use:smoothScroll style="text-decoration: none; color: rgba(227, 242, 253, 0.9);">Research Questions</a>
            <a href="#data" use:smoothScroll style="text-decoration: none; color: rgba(227, 242, 253, 0.9);">Data</a>
            <a href="#hypothesis" use:smoothScroll style="text-decoration: none; color: rgba(227, 242, 253, 0.9);">Hypothesis</a>
            <a href="#team" use:smoothScroll style="text-decoration: none; color: rgba(227, 242, 253, 0.9);">Team</a>
        </div>
    </nav>
</header>
<main style="font-family: Poppins, sans-serif; background-color: #f0f4f8; color: #023e8a;">
    <section id="home" style="padding: 3rem; background-image: url('commercial-fishing.jpg'); text-align: center; background-size: cover; background-position: center; height: 50vh; ">
        <h1 style="font-size: 3rem; color: #0077b6; margin: 0; position: relative; top: 90% ;bottom: 0%;">
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
            <span style="font-weight: bold; text-shadow:2px 2px #023e8a;">SDG 14:</span>
            <span style="font-style: italic; color: #023e8a; text-shadow: 2px 2px #0077b6">Life Below Water</span>
            </div>
        </h1>
    </section>
    <section id="bg_of_study" style="background-color: #e0f7fa; padding: 2rem;">    
        <div style="display: flex; justify-content: center; align-items: flex-start; gap: 2rem;">
            <h2 style="font-size: 30pt; color: #0077b6; flex: 1; position:absolute top:50%">Background of the Study</h2>
            <div style="text-align: left; max-width: 800px; padding: 1rem; background-color: #e3f2fd; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); flex: 2;">
                <p style="font-size: 12pt; color: #023e8a; margin: 1rem 0; line-height: 1.6;">The goal of SDG 14: Life Below Water is to examine fish production trends in the Philippines, a country where fisheries are essential for community livelihoods, food security, and economic growth. This study seeks to understand how these trends have evolved over time in response to anthropogenic and environmental stresses by examining the total volume of fish production as well as that of the top five most produced species in the Philippines. The insights that will be produced by the study will be vital for guiding sustainable fisheries management that will aid in the preservation of marine life.</p>
            </div>
        </div>
    </section>  
    <section id="research_qs" style="padding: 2rem; background-image: url('/rsq_bg.jpg'); background-size: cover; background-position: center;">
        <center>       
            <h2 style="font-size: 30pt; color: #0077b6; margin-bottom: 1rem; text-shadow: 2px 2px #023e8a">Research Questions</h2>
            <div style="text-align: left; max-width: 800px; margin: 0 auto; padding: 1rem; background-color: rgba(227, 242, 253, 0.9); border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 20pt; color: #023e8a; margin: 1rem 0; line-height: 1.6;">
                    <strong>1.</strong> What is the trend in the volume of overall fish production in the Philippines?
                </p>
                <p style="font-size: 20pt; color: #023e8a; margin: 1rem 0; line-height: 1.6;">
                    <strong>2.</strong> What is the trend in the volume of production of the top 5 most produced fish species in the Philippines?
                </p>
            </div>
        </center>
    </section>

    <section id="data" style="padding: 2rem; background-color: #e0f7fa;">
        <center>
            <h2 style="font-size: 50pt; color: #0077b6; margin-bottom: 1rem;">Data Collection</h2>  
            <h3 style="text-align: justify;">
                This datasheet was gathered from
                <a href="https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__2E__FS/?tablelist=true&rxid=bdf9d8da-96f1-4100-ae09-18cb3eaeb313t" style="color: #0077b6">Philippine Statistics Authority OpenSTAT</a>
                database. We downloaded the <b>Volume of Production</b> by Geolocation, Species, Year and Quarter for <b>Commercial Fisheries</b> from <b>2002 - 2024</b>. Since there was a limitation to the amount of rows in the data that can be downloaded. We compiled the data and put it into one sheet.
                We used Google Sheets to compile the data and make it easier to analyze.
            </h3>
            <br>
            <a href="https://docs.google.com/spreadsheets/d/15alTvlMrqoV4MNON0ckjl3GKos50J2l0/edit?gid=630430885#gid=630430885" 
            style="font-size: 20pt; background-color: #7cceff; color: #ffffff; text-decoration: none; padding: 10px 10px; border-radius: 5px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
             Go to datasheet
            </a>
        </center>
    </section>

    <section id="hypothesis" style="padding: 2rem; background-color: #caf0f8;">
        <center>
            <h2 style="font-size: 50pt; color: #0077b6; margin-bottom: 1rem;">Hypothesis</h2>
            <div style="text-align: left; max-width: 800px; margin: 0 auto; padding: 1rem; background-color: #e3f2fd; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 20pt; color: #023e8a; margin: 1rem 0; line-height: 1.6;">
                    <strong>Alternative Hypothesis:</strong>
                    There is a positive trend in the volume of production of different species of fish in the Philippines per year.
                </p>
                <p style="font-size: 20pt; color: #023e8a; margin: 1rem 0; line-height: 1.6;">
                    <strong>Null Hypothesis:</strong>
                    There is no significant trend in the volume of production of different species of fish in the Philippines per year.
                </p>
            </div>
        </center>
    </section>
    <section id="team" style="padding: 2rem; background-color: #e0f7fa;">
        <center>
            <h2 style="font-size: 50pt; color: #0077b6; margin-bottom: 1rem;">Team</h2>
            <div style="display: flex; justify-content: center; gap: 1rem;">
                <div style="flex: 1; padding: 1rem; background-color: #e3f2fd; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <h3 style="font-size: 20pt; color: #0077b6; margin-bottom: 1rem;">Dale Sealtiel Flores</h3>
                    <p style="font-size: 14pt; color: #023e8a; text-align:justify">I am a 2nd year BS CS student from UP Diliman. I am currently in the process of finding what field of computer science I want to get into. I have somewhat dabbled in web development and data science.</p>
                </div>
                <div style="flex: 1; padding: 1rem; background-color: #e3f2fd; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <h3 style="font-size: 20pt; color: #0077b6; margin-bottom: 1rem;">Aaron Jori Baclor</h3>
                    <p style="font-size: 14pt; color: #023e8a; text-align:justify">Description about Member 2.</p>
                </div>
                <div style="flex: 1; padding: 1rem; background-color: #e3f2fd; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                    <h3 style="font-size: 20pt; color: #0077b6; margin-bottom: 1rem;">Sebastian Lucian Reyes</h3>
                    <p style="font-size: 14pt; color: #023e8a; text-align:justify">Description about Member 3.</p>
                </div>
            </div>
        </center>
</main>

