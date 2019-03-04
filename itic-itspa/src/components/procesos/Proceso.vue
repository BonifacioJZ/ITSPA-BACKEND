<template>
    <div>
        <v-timeline align-top>
            <v-timeline-item
            v-for="(proceso,i) in Procesos"
            :key="i"
            :color="proceso.color"
            :icon="proceso.icon"
            fill-dot>
                <v-card
                    :color="proceso.color">
                    <v-card-title class="tittle" >{{ proceso.titulo }}</v-card-title>
                    <v-card-text class="white text--primary" >
                        <p>{{ proceso.descripcion }}</p>
                        <v-btn
                        v-if="proceso.archivo==1"
                        :color="proceso.color"
                        class="mx-0"
                        outline
                        >
                        Button
                        </v-btn>
                    </v-card-text>
                    
                </v-card>

            </v-timeline-item>
        </v-timeline>
        
    </div>
</template>

<script>
export default {
    name:"proceso",
    props:{
        Procesos:Array
    }
}
</script>