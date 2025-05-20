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
<header style="display: flex; align-items: center; justify-content: space-between; padding: 1rem; font-family:Bebas Neue, sans-serifs;">
    <h1>
        <div style="display: flex; align-items: center; gap: 0.5rem">
            <a href="https://www.flaticon.com/free-icons/nemo" title="nemo icons">
            <img src="/fishing-net 1.png" alt="Fishing Net"/>
            </a>
            <span>Net Gains</span>
        </div>
    </h1>
    <nav>
        <div style="display: flex; gap: 1rem;"> 
            <a href="#home" use:smoothScroll >Home</a>
            <a href="#research_qs" use:smoothScroll>Research Questions</a>
            <a href="#data" use:smoothScroll>Data</a>
            <a href="#hypothesis" use:smoothScroll>Hypothesis</a>
            <a href="#team" use:smoothScroll>Team</a>
        </div>
    </nav>
</header>

<main>
    <section id="home">
        <img src="home_bg.jpg" alt="Background">
    </section>
    <section id="title">
        <div class="sdg14icon"><img class="sdg-icon" src="life_below_water.png" alt="SDG 14" /></div>
        <div class="line"></div>
        <div class="sdg14"><span class="sdg14title">SDG 14<br/>Life Below Water</span>
        <span class="studytitle">Analyzing Fish Production <br/>Trends in the Philippines: <br/>A Data-Driven Approach</span></div>
    </section>

    
    <section id="rsq">
           <div class="rsqtitle">Research <br>Questions</div>
           <div class=rsqcontent>
                <p>
                    <strong>1.</strong> What is the trend in the volume of overall fish production in the Philippines?
                </p>
                <p>
                    <strong>2.</strong> What is the trend in the volume of production of the top 5 most produced fish species in the Philippines?
                </p>
            </div>
    </section>
    
    <section id="data">
            <div class="datatitle">Data Collection</div>
            <div class="datacontent">
                <div class="datadescription">
                This datasheet was gathered from
                <a href="https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__2E__FS/?tablelist=true&rxid=bdf9d8da-96f1-4100-ae09-18cb3eaeb313t" style="color: #0077b6">Philippine Statistics Authority OpenSTAT</a>
                database. We downloaded the <b>Volume of Production</b> by Geolocation, Species, Year and Quarter for <b>Commercial Fisheries, Inland, Aquaculture, Municipal Inland Fisheries</b> from <b>2002 - 2024</b>. Since there was a limitation to the amount of rows in the data that can be downloaded. We compiled the data and put it into one sheet.
                We used Google Sheets to compile the data and make it easier to analyze.
                </div>
                <div>
                    
                </div>
            </div>
    </section>
    <section id="bg_of_study">    
        <div>
            <h2 style="font-size: 30pt; color: #0077b6; flex: 1; position:absolute top:50%">Background of the Study</h2>
            <div style="text-align: left; max-width: 800px; padding: 1rem; background-color: #e3f2fd; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); flex: 2;">
                <p style="font-size: 12pt; color: #023e8a; margin: 1rem 0; line-height: 1.6;">The goal of SDG 14: Life Below Water is to examine fish production trends in the Philippines, a country where fisheries are essential for community livelihoods, food security, and economic growth. This study seeks to understand how these trends have evolved over time in response to anthropogenic and environmental stresses by examining the total volume of fish production as well as that of the top five most produced species in the Philippines. The insights that will be produced by the study will be vital for guiding sustainable fisheries management that will aid in the preservation of marine life.</p>
            </div>
        </div>
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

