<script lang="ts">
  // Keep your original smooth scroll functionality
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

  // Add mobile menu toggle functionality
  let mobileMenuOpen = false;
  
  function toggleMobileMenu() {
    mobileMenuOpen = !mobileMenuOpen;
  }

  // Close mobile menu after clicking a link
  function closeMenu() {
    mobileMenuOpen = false;
  }
</script>

<header class={mobileMenuOpen ? "menu-open" : ""}>
    <h1>
        <div style="display: flex; align-items: center; gap: 0.5rem">
            <a href="https://www.flaticon.com/free-icons/nemo" title="nemo icons">
            <img src="/fishing-net 1.png" alt="Fishing Net"/>
            </a>
            <span>Net Gains</span>
        </div>
    </h1>
    <button class="mobile-menu-button" on:click={toggleMobileMenu} aria-label="Toggle menu">
        <!-- Simple hamburger icon -->
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
    </button>
    <nav>
        <div style="display: flex; gap: 1rem;"> 
            <a href="#home" use:smoothScroll on:click={closeMenu}>Home</a>
            <a href="#research_qs" use:smoothScroll on:click={closeMenu}>Research Questions</a>
            <a href="#data" use:smoothScroll on:click={closeMenu}>Data</a>
            <a href="#hypothesis" use:smoothScroll on:click={closeMenu}>Hypothesis</a>
            <a href="#team" use:smoothScroll on:click={closeMenu}>Team</a>
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
        <span class="studytitle">Philippine Fisheries<br/>Through Data: <br/>Trends, Patterns, Insights</span></div>
    </section>


<section id="bg_of_study">
        <div class="bg-title">Background of the Study</div>
        <div class="bg-content">
            <div class="bg-description">
                The Philippines, being an archipelagic country, derives a significant portion of its overall annual food consumption from fish, 
                other seafoods, and aquatic products; up to 22.5% of the average Filipino's diet comes from fish products<a href="https://doi.org/10.35229/jaes.944292" target="_blank">[1]</a>. 
                However, despite this significance, the Philippines has yet to achieve self-sufficiency as in 2024, 25,000 metric tons of fish were set to be imported<a href="https://www.philstar.com/headlines/2024/04/25/2350281/da-philippines-import-25000-mt-fish" target="_blank">[2]</a>; 
                it is therefore only natural to ask how far are the Philippines' domestic fish and seafood product industries from achieving self-sufficiency. 
                Monitoring aquatic food production is important not only economically, but also ecologically; 
                a review paper found that destructive fishing practices such as dynamite fishing, cyanide fishing, and muro-ami fishing were prevalent and remained a lingering problem in the Philippines from the 1930s up until the present date<a href="https://doi.org/10.29329/actanatsci.2022.352.04" target="_blank">[3]</a>. 
                These concerns warrant an investigation into the scale of both destructive and non-destructive fishing practices in the name of assessing sustainability. 
                The economic significance of fish and seafood product industries lies not only in the provision of food, but also in their contribution to employment; 
                from 2021 to 2025, it was found that there was an average of 1,313,000 people employed in these industries at any given month   <a href="https://www.ceicdata.com/en/philippines/labour-force-survey-employment-by-industry-occupation-and-class/employment-agriculture-fishing--aquaculture" target="_blank">[4]</a>; 
                with such a sizeable and significant industry, one may then be inclined to ask regarding the projections of how might this industry grow in the foreseeable future. These questions may be helped answered by first answering the overarching question of this project: 
                what is the trend in the volume of fish product production in the Philippines?
            </div>
        </div>
    </section>

    <section id="rsq">
           <div class="rsqtitle">Research <br>Questions</div>
           <div class="rsqcontent">
                <p>
                    <strong>1.</strong> What is the trend in the volume of overall fish production per fishing sector in the Philippines?
                </p>
                <p>
                    <strong>2.</strong> What is the trend in the volume of overall fish production per region in the Philippines?
                </p>
            </div>
    </section>

    <section id="hypothesis">
        <div class="hypothesis-title">Hypothesis</div>
        <div class="hypothesis-content">
            <div class="hypothesis-box null">
                <h3>Null Hypothesis (H<sub>0</sub>)</h3>
                <ul>
                    <li>There is no significant trend in the volume of overall fish production of the different fisheries sector in the Philippines from 2002 to 2024 per year.</li>
                    <li>There is no significant trend in the volume of overall fish production of the different fisheries sector in the Philippines from 2002 to 2024 per region.</li>
                </ul>
            </div>
            <div class="hypothesis-box alternative">
                <h3>Alternative Hypothesis (H<sub>1</sub>)</h3>
                <ul>
                    <li>There is a significant increasing trend in the volume of overall fish production of the different fisheries sector in the Philippines from 2002 to 2024 per year.</li>
                    <li>There is a significant increasing trend in the volume of overall fish production of the different fisheries sector in the Philippines from 2002 to 2024 per region.</li>
                </ul>
            </div>
        </div>
    </section>

    <section id="data">
        <div class="datatitle">Data Collection</div>
        <div class="datacontent">
            <div class="datadescription">
                This datasheet was gathered from
                <a href="https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__2E__FS/?tablelist=true&rxid=bdf9d8da-96f1-4100-ae09-18cb3eaeb313t" style="color: #0077b6">Philippine Statistics Authority OpenSTAT</a>
                database. We downloaded the <b>Volume of Production</b> by Geolocation, Species, Year and Quarter for <b>Commercial Fisheries, Inland, Aquaculture, Municipal Inland Fisheries</b> from <b>2002 - 2024</b>.
                We used Python's <b><u>pandas</u></b> library to clean and preprocess the data to be used for analysis. THe data was then exported to a Google Sheets document for easy access and visualization.
            </div>
            
            <div class="googlesheet-container">
                <iframe 
                    style="width: 100%; height: 550px; border: none; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" 
                    src="https://docs.google.com/spreadsheets/d/17ge-9f930rXhP0-NKJMFa58Jp_6D-CncS1kNnUMI-ZA/edit?gid=1323382287#gid=1323382287;headers=false"
                    title="Google Sheets Data">
                </iframe>
                <div class="sheet-button-container">
                    <a href="https://docs.google.com/spreadsheets/d/17ge-9f930rXhP0-NKJMFa58Jp_6D-CncS1kNnUMI-ZA/edit?gid=1323382287" target="_blank" class="view-sheet-button">
                        View Full Spreadsheet
                    </a>
                </div>
            </div>
        </div>
    </section>

    <section id="results">
        <div class="results-title">Statistical Results</div>
        <div class="results-content">
            <div class="results-description">
                Python's <b><u>scipy.stats</u></b> library was used to perform statistical analysis on the data. We used the <b>linregress</b> function to perform linear regression on the data, which provided us with the slope, intercept, r-value, p-value, and standard error of the regression line.
            </div>
            
            <div class="results-grid">
                <div class="result-box">
                    <h3>Overall Fish Production Trend per Sector</h3>
                    <p><b>Commercial Fisheries: </b> Slope: -65.7368, p-value: 0.0021, Std Err: 21.3494</p>
                    <img src="commercial-graph.jpg" alt="Commercial Fisheries Trend" />
                    <div class="result-divider"></div>
                    <p><b>Aquaculture: </b> Slope: 70.6809, p-value: 0.00197, Std Err: 22.8399</p>
                    <img src="aquaculture-graph.jpg" alt="Aquaculture Trend" />
                    <div class="result-divider"></div>
                    <p><b>Fisheries: </b> Slope: 2.3524, p-value: 0.9581, Std Err: 44.8246</p>
                    <img src="fisheries-graph.jpg" alt="Fisheries Trend" />
                    <div class="result-divider"></div>
                    <p><b>Marine Municipal Fisheries: </b> Slope: -30.0321, p-value: 0.0043, Std Err: 10.52</p>
                    <img src="marine-municipal-graph.jpg" alt="Marine Municipal Fisheries Trend" />
                    <div class="result-divider"></div>
                    <p><b>Inland Municipal Fisheries: </b> Slope: 1.4145, p-value: 0.6760, Std Err: 3.3847</p>
                    <img src="inland-graph.jpg" alt="Inland Municipal Fisheries Trend" />
                </div>
                
                <div class="result-box">
                    <h3>Overall Fish Production Trend Interpretation</h3>
                    <p style="text-align:justify">The results show that there are trends in commercial, aquaculture, and marine municipal fisheries. Given the negative slope for the <b><u>commercial and marine municipal fisheries</u></b>, it shows that there is a <b><u>negative trend</u></b> in production for these sectors, while there is a <b><u>positive trend</u></b>  in production for <b><u>aquaculture</u></b></p>.
                    <p style="text-align:justify">The <b><u>fisheries and inland municipal fisheries</u></b> sectors do not show any significant trends, as indicated by their p-values being greater than 0.05. This suggests that the production in these sectors has remained relatively stable over the years and there is no trend in their production</p>
                </div>
                <div class="result-box">
                    <h3>Overall Fish Production per Region Geospatial Graph</h3>
                    <p><b>Commercial Fisheries: </b></p>
                    <img src="commercial-geospatial.jpg" alt="Commercial Fisheries Geospatial" />
                    <div class="result-divider"></div>
                    <p><b>Aquaculture: </b></p>
                    <img src="aquaculture-geospatial.jpg" alt="Aquaculture Geospatial" />
                    <div class="result-divider"></div>
                    <p><b>Fisheries: </b></p>
                    <img src="fisheries-geospatial.jpg" alt="Fisheries Geospatial" />
                    <div class="result-divider"></div>
                    <p><b>Marine Municipal Fisheries: </b></p>
                    <img src="marine-geospatial.jpg" alt="Marine Municipal Fisheries Geospatial" />
                    <div class="result-divider"></div>
                    <p><b>Inland Municipal Fisheries: </b></p>
                    <img src="inland-geospatial.jpg" alt="Inland Municipal Fisheries Geospatial" />
                </div>
                
                <div class="result-box">
                    <h3>Overall Fish Production per Region</h3>
                    <p style="text-align:justify"><strong>Top producers are coastal/island regions:</strong></p>
                    <ul>
                        <li><strong>ARMM (Autonomous Region in Muslim Mindanao):</strong> ~35.98 M (19.1% of national total)</li>
                        <li><strong>Region IX (Zamboanga Peninsula):</strong> ~25.32 M (13.4%)</li>
                        <li><strong>Region IV-B (MIMAROPA):</strong> ~24.18 M (12.8%)</li>
                        <li><strong>Region VI (Western Visayas):</strong> ~16.25 M (8.6%)</li>
                        <li><strong>Region IV-A (CALABARZON):</strong> ~14.49 M (7.7%)</li>
                    </ul>
                    <p style="text-align:justify">Together these five regions account for ≈62% of all production, reflecting their extensive coastlines, rich fishing grounds, and well-developed aquaculture.</p>
                    
                    <p style="text-align:justify"><strong>Mid-tier contributors:</strong> Regions XII (SOCCSKSARGEN), III (Central Luzon), V (Bicol), VII (Central Visayas), and VIII (Eastern Visayas) each contribute between 3.6% and 7.0% of the total, with Region XII owing 39.53% of their total in commercial fishing (highest percentage from commercial fishing) and the other mid-tier contributors also boasting increased percentages from municipal fishing.</p>
                    
                    <p style="text-align:justify"><strong>Minimal contributors:</strong></p>
                    <ul>
                        <li><strong>CAR (Cordillera Administrative Region):</strong> 0.16 M (0.08%)</li>
                        <li><strong>Region II (Cagayan Valley):</strong> 2.33 M (1.2%)</li>
                        <li><strong>NCR (Metro Manila):</strong> 2.65 M (1.4%)</li>
                    </ul>
                    <p style="text-align:justify">These regions lack significant marine access (CAR is entirely landlocked) or have undergone rapid urbanization (NCR), leaving little room for large-scale fisheries.</p>

                    <div class="interpretation-section">
                        <h4>Interpretation</h4>
                        <p style="text-align:justify"><strong>Concentration in the south and major island groups:</strong> Regions with extensive coastal waters (Mindanao, Visayas island groups, MIMAROPA) dominate fish output, both from marine capture fisheries and aquaculture.</p>
                        <p style="text-align:justify"><strong>Economic and infrastructural factors:</strong> The top regions have long-established fishing traditions, port facilities, and supportive aquaculture industries (pond culture, cages).</p>
                        <p style="text-align:justify"><strong>Resource and policy implications:</strong> Regions in the mid-tier contributors have room to increase their outputs, and thus could benefit from efforts on boosting production while also adopting sustainable practices to avoid overfishing further marine degradation. Landlocked areas will remain peripheral in fisheries unless inland aquaculture is significantly developed.</p>
                        <p style="text-align:justify"><strong>Equity and food-security angle:</strong> Given the heavy reliance on a handful of regions, diversifying production zones and improving infrastructure in underperforming coastal provinces could enhance resilience against localized shocks (e.g., typhoons, overfishing).</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="team">
        <div class="team-title">Team</div>
        <div class="team-content">
            <div class="team-member">
                <img src="dale.jpg" alt="Dale Sealtiel Flores">
                <h3>Dale Sealtiel Flores</h3>
                <p>I am a 2nd year BS CS student from UP Diliman. I am currently in the process of finding what field of computer science I want to get into. I have somewhat dabbled in web development and data science.</p>
            </div>
            <div class="team-member">
                <img src="aaron.jpg" alt="Aaron Jori Baclor">
                <h3>Aaron Jori Baclor</h3>
                <p>I'm a Computer Science sophomore at UP Diliman. These days, I'm focusing more on myself and paying attention to the things that genuinely make me happy. I enjoy working on personal improvement—whether that's through gaming, basketball, or going to the gym.</p>
                <p>I'm still figuring out which direction I want to take in tech, but I'm taking my time learning and exploring what clicks. For now, I'm just trying to stay consistent and enjoy the process.</p>
            </div>
            <div class="team-member">
                <img src="/sebastian-profile.jpg" alt="Sebastian Lucian Reyes">
                <h3>Sebastian Lucian Reyes</h3>
            </div>
        </div>
    </section>
</main>

<style>
    /* Add any component-specific styles here if needed */
    .mobile-menu-button {
        background: none;
        border: none;
        color: white;
        cursor: pointer;
        padding: 0.5rem;
    }
    
</style>