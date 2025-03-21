<script lang="ts">

   function scrollIntoView(event: Event) {
        const target = event.target as HTMLElement;
        const el = document.querySelector(target.getAttribute('href')!);
        if (!el) return;
    el.scrollIntoView({
      behavior: 'smooth'
    });
  }

</script>
<header>
    <nav>
        <div>
            <a href="#home" onclick={scrollIntoView}>Home</a>
            <a href="#research_qs" onclick={scrollIntoView}>Research Questions</a>
            <a href="#data" onclick={scrollIntoView}>Data</a>
            <a href="#hypothesis" onclick={scrollIntoView}>Hypothesis</a>
        </div>
    </nav>
</header>
<main>
    <section id="home" style="padding: 2rem; background-color: #caf0f8; text-align: center;">
        <h1 class="site-title" style="font-size: 3rem; color: #0077b6; margin: 0;">
            <span class="sdg" style="font-weight: bold;">SDG 14:</span>
            <span class="subtitle" style="font-style: italic; color: #023e8a;">Life Below Water</span>
        </h1>
    </section>
    <section id="research_qs" style="padding: 2rem; background-color: #f0f8ff;">
        <center>
            <h2 style="font-size: 50pt; color: #0077b6; margin-bottom: 1rem;">Research Questions</h2>
            <div style="text-align: left; max-width: 800px; margin: 0 auto; padding: 1rem; background-color: #e3f2fd; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
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
            <h2 style="font-size: 50pt; color: #0077b6; margin-bottom: 1rem;">Datasheet</h2>
            <a href="https://docs.google.com/spreadsheets/d/15alTvlMrqoV4MNON0ckjl3GKos50J2l0/edit?gid=630430885#gid=630430885" 
               style="font-size: 50px; background-color: #7cceff; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                Google Sheets
            </a>
        </center>
    </section>

    <section id="hypothesis" style="padding: 2rem; background-color: #caf0f8;">
        <center>
            <h2 style="font-size: 50pt; color: #0077b6; margin-bottom: 1rem;">Hypothesis</h2>
            <div style="text-align: left; max-width: 800px; margin: 0 auto; padding: 1rem; background-color: #e3f2fd; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <p style="font-size: 20pt; color: #023e8a; margin: 1rem 0; line-height: 1.6;">
                    <strong>Alternative Hypothesis:</strong>
                    There is a significant trend in the volume of production of different species of fish in the Philippines per year, either increasing or decreasing.
                </p>
                <p style="font-size: 20pt; color: #023e8a; margin: 1rem 0; line-height: 1.6;">
                    <strong>Null Hypothesis:</strong>
                    There is no significant trend in the volume of production of different species of fish in the Philippines per year.
                </p>
            </div>
        </center>
</main>

