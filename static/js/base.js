import styles from '../css/index.module.css'


export function activeHome(){
  let home = <li className="nav-item">
    <a className={`nav-link ${styles.aFontStyle}`} style={{textAlign: 'right'}} aria-current="page" href="/home" >Home</a></li>;

  if (window.location.href === 'http://localhost:3000/'){
    home = <li className="nav-item">
    <a className={`nav-link ${styles.aFontStyle} ${styles.navbarActive}`} style={{textAlign: 'center'}} aria-current="page" href="/home" >Home</a></li>
    return home;
  }
    return home;
}

export function activeArtikel(){
  let artikel = <li className="nav-item">
    <a className={`nav-link ${styles.aFontStyle}`} href="/artikel">Artikel</a></li>;


  if (window.location.href === 'http://localhost:3000/artikel'){
    artikel = artikel = <li className="nav-item">
    <a className={`nav-link ${styles.aFontStyle} ${styles.navbarActive}`}><Link to='/artikel'>Artikel</Link></a></li>;
    return artikel;
  }
    return artikel;
}

export function activeJadwalSertifikasi (){
  let jadwalSertifikasi = <li className="nav-item">
    <a className={`nav-link ${styles.aFontStyle}`} style={{width: '10vw'}} href="/jadwal">Jadwal Sertifikasi</a></li>;

  if (window.location.href === 'http://localhost:3000/jadwalsertifikasi'){
    jadwalSertifikasi = <li className="nav-item">
    <a className={`nav-link ${styles.aFontStyle} ${styles.navbarActive}`} style={{width: '10vw', minWidth: '147px'}} href="/jadwal">Jadwal Sertifikasi</a></li>;
    return jadwalSertifikasi;
  }
    return jadwalSertifikasi;
}

export function activePortofolio (){
  let portofolio = <li className="nav-item">
    <a className={`nav-link ${styles.aFontStyle}`} href="#">Portofolio</a></li>;

  if (window.location.href === 'http://localhost:3000/portofolio'){
    portofolio = <li className="nav-item">
    <a className={`nav-link ${styles.aFontStyle} ${styles.navbarActive}`} href="#">Portofolio</a></li>;
    return portofolio;
  }
    return portofolio;
}
