
// static/src/app/store/pos_store.js
/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {
    get idleTimeout() {
        // Повертаємо порожній список таймаутів для відключення SaverScreen
        return [];
    },
});