const { Router } = require('express')
const routes = Router()

/**
 * Controllers
 */
const Main = require('./controllers/main')

/**
 * Routes
 */
routes.get('/', Main.get)

module.exports = routes
