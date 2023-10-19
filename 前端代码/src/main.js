import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/styles/index.scss'
import SvgIcon from '@/icons'
import 'element-plus/dist/index.css'
import * as ELIcons from '@element-plus/icons-vue'
import i18n from '@/i18n'

import axios from 'axios'
import VueAxios from 'vue-axios'
axios.defaults.baseURL = 'http://localhost:5000'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

const app = createApp(App)
app.use(VueAxios, axios)
for (const iconName in ELIcons) {
  app.component(iconName, ELIcons[iconName])
}
SvgIcon(app)
app.use(store).use(router).use(i18n).mount('#app')
